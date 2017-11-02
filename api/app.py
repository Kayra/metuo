import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import exifread


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

    if "file" not in request.files:
        return "No image found"

    image = request.files["file"]

    if image.filename == "":
        return "No image or image name"

    if image and allowed_image(image.filename):

        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        return "Image uploaded"
