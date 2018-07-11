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


@bp.route("/images", methods=["GET"])
def get_images():

    request_tags = request.args['tags'].split(',')

    tags = Tag.query.filter(Tag.tag_name.in_(request_tags)).distinct()
    images = set([tag.images for tag in tags][0])

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_locations = [os.path.join(image_directory, image.name) for image in images]

    return send_file(image_locations[0],
                     attachment_filename=images[0].name,
                     mimetype='image/jpg')


@bp.route("/image", methods=["GET"])
def get_image():

    image_name = request.args.get('image_name')

    try:
        image = Image.query.filter_by(name=image_name).first()
    except Exception as exception:
        return f"Unable to get image due to {exception}"

    return f'<img src="{url_for("static", filename=image.name)}">'
