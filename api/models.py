from api import db


association_table = db.Table('image_tag_association',
                             db.Column('image_id', db.Integer, db.ForeignKey('images.id'), primary_key=True),
                             db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True))


class Image(db.Model):

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    exif_data = db.Column(db.JSON)

    tags = db.relationship('Tag', secondary=association_table, lazy='subquery',
                           backref=db.backref('images', lazy=True))


class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String, unique=True)
