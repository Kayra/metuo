from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import exifread


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://metuo:local_insecure_password@localhost:5432/metuo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = "./"

db = SQLAlchemy(app)


@app.route("/")
@app.route("/index")
def index():
    return "Hello world"


@app.route("/upload")
def upload():
    # Read exif data
    return "Image uploaded"
