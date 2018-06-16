import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy


def init_app_db(app):
    app.cli.add_command(init_db_command)


def get_db():

    if 'db' not in g:
        g.db = SQLAlchemy(current_app)

    return g.db


def init_db():
    db = get_db()
    db.create_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
        Clear the existing data and create new tables.
    """
    from api import models
    init_db()
    click.echo('Successfully initialised the database.')
