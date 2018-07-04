import os
import io

from flask import current_app as app
from werkzeug.utils import secure_filename
from PIL import Image as PILImage, ExifTags

from api.models import Image, db


def save_image(image_hex_bytes):

    image = _hex_to_image(image_hex_bytes)
    exif_data = _format_exif_data(image.getexif())

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_name = secure_filename('test.jpg')
    image_location = os.path.join(image_directory, image_name)

    image.save(image_location)

    db_image = Image(name=image_name,
                     exif_data=exif_data)

    db.session.add(db_image)
    db.session.commit()


def _hex_to_image(image_hex_bytes):

    image_stream = io.BytesIO(image_hex_bytes)
    image = PILImage.open(image_stream)

    return image


def _format_exif_data(unformatted_exif_data):

    return {
        ExifTags.TAGS[exif_index]: str(exif_data, 'utf-8') if isinstance(exif_data, bytes) else exif_data
        for exif_index, exif_data in unformatted_exif_data.items()
        if exif_index in ExifTags.TAGS
    }


# def allowed_image(image_name):
#
#     try:
#         image_extension = image_name.rsplit(".", 1)[1].lower()
#     except IndexError:
#         return False
#
#     return image_extension in ALLOWED_EXTENSIONS
