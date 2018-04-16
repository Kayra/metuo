import os
import io

import exifread
from PIL import Image
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://metuo:local_insecure_password@localhost:5432/metuo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["UPLOAD_FOLDER"] = "./"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)


def allowed_image(image_name):

    try:
        image_extension = image_name.rsplit(".", 1)[1].lower()
    except IndexError:
        return False

    return image_extension in ALLOWED_EXTENSIONS


@app.route("/")
@app.route("/index")
def index():
    return "Hello world"


@app.route("/upload", methods=["POST"])
def upload_image():

    # Read exif data

    if not request.data:
        return "No image found"

    try:
        save_hex_as_image(request.data)
    except:
        return "Unable to upload image"

    return "Image uploaded"

    # with open('test.jpeg', 'w+') as image:
    #     image.write(request.data.decode('base64'))


    # image = Image.frombytes(request.data)
    # print("HIT", image)
    #
    # if image.filename == "":
    #     return "No image or image name"
    #
    # if image and allowed_image(image.filename):
    #
    #     image_name = secure_filename(image.filename)
    #     image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
    #

def save_hex_as_image(image_hex_bytes, save_location=''):

    image_stream = io.BytesIO(image_hex_bytes)
    image = Image.open(image_stream)
    image.save(os.path.join(save_location, 'test.jpeg'))
