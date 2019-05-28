import json

from flask import Blueprint, request, jsonify, abort, make_response

from server.models import Tag, Image
from server.helpers import save_image, build_categorised_tags, remove_image


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
        json_response.update(image.to_json())

    return jsonify(json_response)


@bp.route("/image/<image_id>", methods=["GET"])
def get_image(image_id):

    if image_id:
        image = Image.query.filter_by(id=image_id).first()
        if image:
            return jsonify(image.to_json())
        else:
            return abort(404)

    return abort(405)


@bp.route("/image/update-tags/<image_id>", methods=["PUT"])
def update_image_tags(image_id):

    tags_to_update = request.get_json()

    if image_id and tags_to_update:
        image = Image.query.filter_by(id=image_id).first()
        if image:
            image.update_tags(tags_to_update)
            return jsonify(image.to_json())
        else:
            return abort(404)

    return abort(405)


@bp.route("/image/delete/<image_id>", methods=["DELETE"])
def delete_image(image_id):

    if image_id:

        if Image.query.filter_by(id=image_id).scalar():
            image_json = Image.query.filter_by(id=image_id).first().to_json()
            remove_image(image_id)
            return make_response(json.dumps({"Image deleted": image_json}), 200)
        else:
            return make_response(f"Couldn't find image {image_id}", 404)

    return abort(405)


@bp.route("/tags", methods=["GET"])
def get_categorised_tags():

    tags = Tag.query.all()
    categorised_tags = build_categorised_tags(tags)

    return jsonify(categorised_tags)
