import json

from flask import Blueprint, request, jsonify, abort

from server.models import Tag, Image
from server.helpers import save_image, build_categorised_tags, load_image


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
        json_response[image.id] = {
            "name": image.name,
            "location": load_image(image.name),
            "categorised_tags": build_categorised_tags(image.tags)
        }

    return jsonify(json_response)


@bp.route("/image", methods=["GET"])
def get_image():

    if request.args.get('id'):

        image = Image.query.filter_by(id=request.args['id']).first()

        response_json = {
            image.id: {
                'name': image.name,
                'exif': image.exif_data,
                "categorised_tags": build_categorised_tags(image.tags),
                "location": load_image(image.name)
            }
        }

        return jsonify(response_json)
    else:
        abort(404)


@bp.route("/tags", methods=["GET"])
def get_categorised_tags():

    tags = Tag.query.all()
    categorised_tags = build_categorised_tags(tags)

    return jsonify(categorised_tags)
