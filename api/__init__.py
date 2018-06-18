import os
from pathlib import Path

from flask import Flask

from api.database import init_app_db
from api.blueprints import images


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://metuo:local_insecure_password@postgres:5432/metuo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    project_root_path = Path(__file__).parent.parent.absolute()
    app.config["IMAGE_DIRECTORY"] = os.path.join(project_root_path, "image_uploads/")
    app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg', 'gif'}

    init_app_db(app)

    app.register_blueprint(images.bp)
    app.add_url_rule('/upload', endpoint='upload_image')
    app.add_url_rule('/images', endpoint='get_images')

    @app.route("/")
    @app.route("/index")
    def index():
        return "Hello world"

    return app
