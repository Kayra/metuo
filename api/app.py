import os
import io

from PIL import Image, ExifTags
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

    if not request.data:
        return "No image found"

    try:
        image = hex_to_image(request.data)
        image.save(os.path.join('./', secure_filename('test.jpg')))

    except Exception as exception:
        return f"Unable to upload image due to {exception}"

    exif_data = format_exif_data(image.getexif())

    return "Image uploaded"


def hex_to_image(image_hex_bytes):

    image_stream = io.BytesIO(image_hex_bytes)
    image = Image.open(image_stream)

    return image


def format_exif_data(unformatted_exif_data):

    return {
        ExifTags.TAGS[exif_index]: exif_data
        for exif_index, exif_data in unformatted_exif_data.items()
        if exif_index in ExifTags.TAGS
    }
