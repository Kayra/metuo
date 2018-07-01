import os

from flask import Blueprint, request, send_file, current_app as app

from api.helpers import save_image
from api.models import Image


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



