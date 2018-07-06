import os
from pathlib import Path

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://metuo:local_insecure_password@postgres:5432/metuo"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    project_root_path = Path(__file__).parent.parent.absolute()
    app.config["IMAGE_DIRECTORY"] = os.path.join(project_root_path, "image_uploads/")
    app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg', 'gif'}

    db.init_app(app)
    app.cli.add_command(init_db_command)

    with app.app_context():
        from api import views
        app.register_blueprint(views.bp)
        app.add_url_rule('/upload', endpoint='upload_image')
        app.add_url_rule('/images', endpoint='get_images')
        app.add_url_rule('/image', endpoint='get_image')

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
    from api import models

    db.drop_all()
    db.create_all()
    click.echo('Successfully initialised the database.')
