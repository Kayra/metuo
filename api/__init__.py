import os
from pathlib import Path

from flask import Flask


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://metuo:local_insecure_password@postgres:5432/metuo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    project_root_path = Path(__file__).parent.parent.absolute()
    app.config["IMAGE_DIRECTORY"] = os.path.join(project_root_path, "image_uploads/")
    app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg', 'gif'}

    @app.route("/")
    @app.route("/index")
    def index():
        return "Hello world"

    return app
