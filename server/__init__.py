import os
from pathlib import Path

import click
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():

    app = Flask(__name__)

    CORS(app)

    postgres_user = os.getenv('RDS_USERNAME')
    postgres_password = os.getenv('RDS_PASSWORD')
    postgres_db = os.getenv('RDS_DB_NAME')
    postgres_host = os.getenv('RDS_HOSTNAME')
    postgres_port = os.getenv('RDS_PORT')

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    image_directory = os.getenv('IMAGE_DIRECTORY', local_static_dir())
    app.config["IMAGE_DIRECTORY"] = image_directory
    app.static_folder = image_directory
    app.static_url_path = 'image_uploads'

    app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg', 'gif'}

    db.init_app(app)
    app.cli.add_command(init_db_command)

    with app.app_context():
        from server import views
        app.register_blueprint(views.bp)

    @app.route("/")
    @app.route("/health")
    def index():
        return "Alive"

    return app


def local_static_dir() -> str:
    project_root_path = Path(__file__).parent.parent.absolute()
    return os.path.join(project_root_path, "image_uploads")


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
        Clear the existing data and create new tables.
    """
    from server import models
    db.drop_all()
    db.create_all()
    click.echo('Successfully initialised the database.')
