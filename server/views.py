import json

from flask import Blueprint, request, jsonify, abort, make_response

from server.models import Tag, Image, User
from server.helpers.image_helpers import save_image, remove_image
from server.helpers.tag_helpers import build_categorised_tags


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
        images = Image.query.limit(20).all()

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


@bp.route("/create_user", methods=["POST"])
def create_user():

    username = request.json['username']
    password = request.json['password']

    if not User.exists(username):

        user = User(username=username, password=password)
        user.save()
        return f"Created user {username}"

    else:
        return f"User {username} exists"


@bp.route("/authenticate_user", methods=["POST"])
def authenticate_user():

    username = request.json['username']
    password = request.json['password']

    if User.exists(username):

        user = User.query.filter_by(username=username).first()
        print(password)
        print(type(password))

        if user.is_correct_password(password):
            return f"Authenticated {username}"
        else:
            return f"Incorrect password for user {username}"

    else:
        return f"User {username} does not exist"
