import os
from pathlib import Path

import click
from flask import Flask
from flask_cors import CORS
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    CORS(app)

    postgres_user = os.environ['POSTGRES_USER']
    postgres_password = os.environ['POSTGRES_PASSWORD']
    postgres_db = os.environ['POSTGRES_DB']
    postgres_host = os.environ['POSTGRES_HOST']
    postgres_port = os.environ['POSTGRES_PORT']

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    project_root_path = Path(__file__).parent.parent.absolute()
    app.config["IMAGE_DIRECTORY"] = os.path.join(project_root_path, "image_uploads")
    app.static_folder = app.config["IMAGE_DIRECTORY"]
    app.static_url_path = 'image_uploads'

    app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg', 'gif'}

    db.init_app(app)
    app.cli.add_command(init_db_command)

    with app.app_context():
        from server import views
        app.register_blueprint(views.bp)
        app.add_url_rule('/upload', endpoint='upload_image')
        app.add_url_rule('/images', endpoint='get_images')
        app.add_url_rule('/tags', endpoint='get_tags')

    @app.route("/")
    @app.route("/health")
    def index():
        return "Alive"

    return app


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
