from flask import Blueprint, request, url_for, jsonify

from api.models import Tag
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

    tags = request.args.get('tags').split(',')

    try:
        images = Tag.get_images(tags)

    except Exception as exception:
        return f"Unable to get image due to {exception}"

    json_response = {}
    for image in images:
        json_response[image.name] = {
            "location": url_for("static", filename=image.name),
            "tags": [tag.name for tag in image.tags]
        }

    return jsonify(json_response)


@bp.route("/tags", methods=["GET"])
def get_tags():
    tags = Tag.query.all()
    return jsonify([tag.name for tag in tags])
