import os
import io

from flask import Blueprint, flash, g, redirect, render_template, request, url_for, send_file, current_app as app
from PIL import Image as PILImage, ExifTags
from werkzeug.utils import secure_filename
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
# from api.database import get_db

from api.models import Image, db


bp = Blueprint('images', __name__)


@bp.route("/upload", methods=["POST"])
def upload_image():

    if not request.data:
        return "No image found"

    try:
        save_image(request.data)

    except Exception as exception:
        return f"Unable to upload image due to {exception}"

    return "Image uploaded"


@bp.route("/images", methods=["GET"])
def get_images():

    image_directory = app.config["IMAGE_DIRECTORY"]
    images = Image.query.all()
    image_locations = [os.path.join(image_directory, image.name) for image in images]

    return send_file(image_locations[0],
                     attachment_filename=images[0].name,
                     mimetype='image/jpg')


# def allowed_image(image_name):
#
#     try:
#         image_extension = image_name.rsplit(".", 1)[1].lower()
#     except IndexError:
#         return False
#
#     return image_extension in ALLOWED_EXTENSIONS


def hex_to_image(image_hex_bytes):

    image_stream = io.BytesIO(image_hex_bytes)
    image = PILImage.open(image_stream)

    return image


def format_exif_data(unformatted_exif_data):

    return {
        ExifTags.TAGS[exif_index]: str(exif_data, 'utf-8') if isinstance(exif_data, bytes) else exif_data
        for exif_index, exif_data in unformatted_exif_data.items()
        if exif_index in ExifTags.TAGS
    }


def save_image(image_hex_bytes):

    image = hex_to_image(image_hex_bytes)
    exif_data = format_exif_data(image.getexif())

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_name = secure_filename('test.jpg')
    image_location = os.path.join(image_directory, image_name)

    image.save(image_location)

    db_image = Image(name=image_name,
                     exif_data=exif_data)

    db.session.add(db_image)
    db.session.commit()
