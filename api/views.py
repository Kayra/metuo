import os

from flask import Blueprint, request, send_file, url_for, current_app as app

from api.models import Image, Tag
from api.helpers import save_image


bp = Blueprint('images', __name__)


@bp.route("/upload", methods=["POST"])
def upload_image():

    if not request.files:
        return "No image found"

    image = request.files['image']
    tags = request.values['tags'].split(',')

    save_image(image, tags)

    return "Image uploaded"


@bp.route("/image", methods=["GET"])
def get_image():

    image_name = request.args.get('image_name')

    try:
        image = Image.query.filter_by(name=image_name).first()
    except Exception as exception:
        return f"Unable to get image due to {exception}"

    return f'<img src="{url_for("static", filename=image.name)}">'
