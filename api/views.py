import os

from flask import Blueprint, request, send_file, current_app as app

from api.models import Image
from api.helpers import save_image


bp = Blueprint('images', __name__)


@bp.route("/upload", methods=["POST"])
def upload_image():

    if not request.files:
        return "No image found"

    try:
        image = request.files.to_dict()['image']
        save_image(image)

    except Exception as exception:
        return f"Unable to upload image due to {exception}"

    return "Image uploaded"


@bp.route("/images", methods=["GET"])
def get_images():

    images = Image.query.all()

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_locations = [os.path.join(image_directory, image.name) for image in images]

    return send_file(image_locations[0],
                     attachment_filename=images[0].name,
                     mimetype='image/jpg')


@bp.route("/image", methods=["GET"])
def get_image():

    image_name = request.args.get('image_name')

    try:
        image = Image.query.filter_by(name=image_name).one()
    except Exception as exception:
        return f"Unable to get image due to {exception}"

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_location = os.path.join(image_directory, image.name)

    return send_file(image_location,
                     attachment_filename=image.name,
                     mimetype='image/jpg')
