import json

from flask import Blueprint, request, url_for, jsonify

from server.models import Tag, Image
from server.helpers import save_image, build_categorised_tags


bp = Blueprint('images', __name__)


@bp.route("/upload", methods=["POST"])
def upload_image():

    if not request.files:
        return "No image found"

    image = request.files['image']
    tags = json.loads(request.values['tags'])

    save_image(image, tags)

    return "Image uploaded"


@bp.route("/images", methods=["GET"])
def get_images():

    tag_string = request.args.get('tags')
    tags = tag_string.split(',') if tag_string else None

    if tags:
        images = Tag.get_images(tags)

    else:
        images = Image.query.limit(5).all()

    json_response = {}
    for image in images:
        json_response[image.name] = {
            "location": url_for("static", filename=image.name),
            "categorised_tags": build_categorised_tags(image.tags)
        }

    return jsonify(json_response)


@bp.route("/tags", methods=["GET"])
def get_categorised_tags():

    tags = Tag.query.all()
    categorised_tags = build_categorised_tags(tags)

    return jsonify(categorised_tags)
