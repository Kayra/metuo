from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import exifread


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://metuo:local_insecure_password@localhost:5432/metuo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["UPLOAD_FOLDER"] = "./"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)


def allowed_file(file_name):

    try:
        file_extension = file_name.rsplit(".", 1)[1].lower()
    except IndexError:
        return False

    return file_extension in ALLOWED_EXTENSIONS


@app.route("/")
@app.route("/index")
def index():
    return "Hello world"


@app.route("/upload")
def upload_image():
    # Read exif data
    return "Image uploaded"
