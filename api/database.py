from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g


def get_db():

    if 'db' not in g:
        g.db = SQLAlchemy(current_app)

    return g.db


def close_db(e=None):

    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.create_all()


