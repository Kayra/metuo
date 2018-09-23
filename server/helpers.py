import os
import io
from typing import Dict, List

from werkzeug import FileStorage
from flask import current_app as app
from werkzeug.utils import secure_filename
from PIL import Image as PILImage, ExifTags
from PIL.JpegImagePlugin import JpegImageFile

from server.models import Image, Category, db


def save_image(image: FileStorage, categorised_tags: Dict):

    image_name = image.filename
    image_hex_bytes = image.read()

    image = _hex_to_image(image_hex_bytes)
    exif_data = _format_exif_data(image.getexif())

    _save_image_locally(image, image_name)

    db_image = Image(name=image_name, exif_data=exif_data)
    db_image.add_tags(categorised_tags)

    db.session.add(db_image)
    db.session.commit()


# def _format_tags(categorised_tags: Dict) -> List[str]:
#
#     formatted_tags = []
#
#     for category, tags in categorised_tags:
#         category_object = Category.query.filter_by(name=category).one() if Category.exists(name=category) else Category(name=category)
#
#     return formatted_tags


def _save_image_locally(image, image_name) -> None:

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_name = secure_filename(image_name)
    image_location = os.path.join(image_directory, image_name)

    image.save(image_location)


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
