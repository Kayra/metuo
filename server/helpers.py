import os
import io
import uuid
from typing import Dict, List

import boto3
from flask import url_for, current_app as app
from werkzeug.datastructures import FileStorage
from PIL import Image as PILImage, ExifTags
from PIL.JpegImagePlugin import JpegImageFile

from server.models import Image, Tag, db


def build_categorised_tags(tags: List[Tag]) -> Dict:

    categorised_tags = {}

    for tag in tags:

        category = tag.category.name
        if category in categorised_tags.keys():
            categorised_tags[category].append(tag.name)
        else:
            categorised_tags[category] = [tag.name]

    return categorised_tags


def save_image(uploaded_image: FileStorage, categorised_tags: Dict):

    image_hex_bytes = uploaded_image.read()
    image = _hex_to_image(image_hex_bytes)
    uploaded_image.seek(0)

    exif_data = _format_exif_data(image.getexif())
    image_name = _generate_image_name(uploaded_image.filename, exif_data)

    if os.getenv('FLASK_DEBUG') == '0':
        _save_image_to_s3_bucket(uploaded_image, image_name)
    else:
        _save_image_locally(image, image_name)

    db_image = Image(name=image_name, exif_data=exif_data)
    db_image.add_tags(categorised_tags)

    db.session.add(db_image)
    db.session.commit()


def load_image(image_name: str) -> str:

    if os.getenv('FLASK_DEBUG') == '0':
        return f"https://metuo-server.s3.eu-west-2.amazonaws.com/{image_name}"
    else:
        return url_for("static", filename=image_name)


def _generate_image_name(file_name: str, exif_data: Dict) -> str:

    string_to_hash = file_name + exif_data['DateTimeOriginal']
    file_extension = file_name.split('.')[-1]
    file_name_hash = str(uuid.uuid5(uuid.NAMESPACE_DNS, string_to_hash))

    return file_name_hash + '.' + file_extension


def _save_image_locally(image: JpegImageFile, image_name: str) -> None:

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_location = os.path.join(image_directory, image_name)

    image.save(image_location)


def _save_image_to_s3_bucket(image: FileStorage, image_name: str) -> None:

    image_directory = app.config["IMAGE_DIRECTORY"]

    s3_client = boto3.client('s3',
                             aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                             aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
    response = s3_client.upload_fileobj(image, image_directory, image_name)

    if response:
        print(response)


def _hex_to_image(image_hex_bytes) -> JpegImageFile:
    
    image_stream = io.BytesIO(image_hex_bytes)
    image = PILImage.open(image_stream)

    return image


def _format_exif_data(unformatted_exif_data):
    return {
        ExifTags.TAGS[exif_index]: str(exif_data, 'utf-8') if isinstance(exif_data, bytes) else exif_data
        for exif_index, exif_data in unformatted_exif_data.items()
        if exif_index in ExifTags.TAGS
    }
