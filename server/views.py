import json

from flask import Blueprint, request, jsonify, abort, make_response
from flask_jwt_extended import jwt_required, create_access_token
from sqlalchemy.sql.expression import func

from server.models import Tag, Image, User
from server.helpers.image_helpers import save_image, remove_image
from server.helpers.tag_helpers import build_categorised_tags


bp = Blueprint('images', __name__)


@bp.route("/images", methods=["GET"])
def get_images():

    tag_string = request.args.get('tags')

    if tag_string:
        images = Tag.get_images(tag_string.split(','))
    else:
        images = Tag.get_images(['Best'])
        if not images:
            images = Image.query.order_by(func.random()).limit(20).all()

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


@bp.route("/upload", methods=["POST"])
@jwt_required()
def upload_image():

    if not request.files:
        return "No image file found"

    image = request.files['image']
    tags = json.loads(request.values['tags'])

    save_image(image, tags)

    return "Image uploaded"


@bp.route("/image/update-tags/<image_id>", methods=["PUT"])
@jwt_required()
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
@jwt_required()
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


# Only uncomment to create a user, then re-comment - MVP ;)
# @bp.route("/create_user", methods=["POST"])
# def create_user():
#
#     username = request.json['username']
#     password = request.json['password']
#
#     if not User.exists(username):
#
#         user = User(username=username, password=password)
#         user.save()
#         return f"Created user {username}"
#
#     else:
#         return f"User {username} exists"


@bp.route("/authenticate_user", methods=["POST"])
def authenticate_user():

    username = request.json['username']
    password = request.json['password']

    if User.exists(username):

        user = User.query.filter_by(username=username).first()

        if user.is_correct_password(password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            return f"Incorrect password for user {username}"

    else:
        return f"User {username} does not exist"
