from pathlib import Path
import os
import io

from PIL import Image as PILImage, ExifTags
from flask import Flask, request, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://metuo:local_insecure_password@postgres:5432/metuo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

PATH = Path(__file__).parent.parent.absolute()
app.config["IMAGE_DIRECTORY"] = os.path.join(PATH, "image_uploads/")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)

if os.environ['FLASK_DEBUG'] == '1':
    import functools
    print = functools.partial(print, flush=True)


class Image(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # location
    exif_data = db.Column(db.JSON)


@app.route("/")
@app.route("/index")
def index():
    return "Hello heejer"


@app.route("/upload", methods=["POST"])
def upload_image():

    if not request.data:
        return "No image found"

    try:
        save_image(request.data)

    except Exception as exception:
        return f"Unable to upload image due to {exception}"

    return "Image uploaded"


@app.route("/images", methods=["GET"])
def get_images():

    image_directory = app.config["IMAGE_DIRECTORY"]
    images = Image.query.all()
    image_locations = [os.path.join(image_directory, image.name) for image in images]

    return send_file(image_locations[0],
                     attachment_filename=images[0].name,
                     mimetype='image/jpg')


def allowed_image(image_name):

    try:
        image_extension = image_name.rsplit(".", 1)[1].lower()
    except IndexError:
        return False

    return image_extension in ALLOWED_EXTENSIONS


def hex_to_image(image_hex_bytes):

    image_stream = io.BytesIO(image_hex_bytes)
    image = PILImage.open(image_stream)

    return image


def format_exif_data(unformatted_exif_data):

    return {
        ExifTags.TAGS[exif_index]: str(exif_data, 'utf-8') if isinstance(exif_data, bytes) else exif_data
        for exif_index, exif_data in unformatted_exif_data.items()
        if exif_index in ExifTags.TAGS
    }


def save_image(image_hex_bytes):

    image = hex_to_image(image_hex_bytes)
    exif_data = format_exif_data(image.getexif())

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_name = secure_filename('test.jpg')
    image_location = os.path.join(image_directory, image_name)

    image.save(image_location)

    db_image = Image(
        name=image_name,
        exif_data=exif_data
    )

    db.session.add(db_image)
    db.session.commit()
