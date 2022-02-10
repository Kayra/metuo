import io
import os
import uuid
from typing import Dict

from flask import url_for
from PIL import Image as PILImage, ExifTags
from PIL.JpegImagePlugin import JpegImageFile
from werkzeug.datastructures import FileStorage

from server.models import Image, db
from server.helpers.app_helpers import is_production, get_exif_datetime
from server.helpers.tag_helpers import update_categorised_tags_with_exif_data
from server.helpers.file_helpers import save_image_file_locally, \
                                        delete_image_file_locally, \
                                        save_image_file_to_s3_bucket, \
                                        delete_image_file_in_s3_bucket


def save_image(uploaded_image: FileStorage, categorised_tags: Dict):

    image_hex_bytes = uploaded_image.read()
    image = _hex_to_image(image_hex_bytes)
    uploaded_image.seek(0)

    exif_data = _format_exif_data(image.getexif())
    updated_categorised_tags = update_categorised_tags_with_exif_data(exif_data, categorised_tags)
    image_name = generate_hashed_image_name(uploaded_image.filename, exif_data)

    if is_production():
        save_image_file_to_s3_bucket(uploaded_image, image_name)
    else:
        save_image_file_locally(image, image_name)

    db_image = Image(name=image_name, exif_data=exif_data)
    db_image.add_tags(updated_categorised_tags)

    db.session.add(db_image)
    db.session.commit()


def remove_image(image_id: str) -> None:

    image = Image.query.filter_by(id=image_id).first()

    if is_production():
        delete_image_file_in_s3_bucket(image.name)
    else:
        delete_image_file_locally(image.name)

    db.session.delete(image)
    db.session.commit()


def load_image(image_name: str) -> str:

    if is_production():
        # return f"https://metuo-server.s3.eu-west-2.amazonaws.com/{image_name}"
        return f"http://d1sq2bjn8ziqtj.cloudfront.net/{image_name}"
    else:
        return url_for("static", filename=image_name, _external=True)


def generate_hashed_image_name(file_name: str, exif_data: Dict) -> str:

    date_string = get_exif_datetime(exif_data)
    string_to_hash = file_name + date_string
    file_extension = os.path.splitext(file_name)[1]
    file_name_hash = str(uuid.uuid5(uuid.NAMESPACE_DNS, string_to_hash))

    return file_name_hash + file_extension


def _hex_to_image(image_hex_bytes) -> JpegImageFile:

    image_stream = io.BytesIO(image_hex_bytes)
    image = PILImage.open(image_stream)

    return image


def _format_exif_data(unformatted_exif_data) -> Dict:

    cast_to_float = ['XResolution', 'YResolution']

    clean_exif = {}
    for exif_index, exif_data in unformatted_exif_data.items():

        exif_index_label = ExifTags.TAGS[exif_index]

        if exif_index in ExifTags.TAGS:
            clean_exif[exif_index_label] = str(exif_data, 'utf-8') if isinstance(exif_data, bytes) else exif_data
        if exif_index_label in cast_to_float:
            clean_exif[exif_index_label] = float(unformatted_exif_data[exif_index])

    return clean_exif
