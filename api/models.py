from typing import List

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

    def add_tags(self, tags: List[str]) -> None:
        for tag in tags:
            tag_object = Tag.query.filter_by(tag_name=tag).one() if Tag.exists(tag_name=tag) else Tag(tag_name=tag)
            self.tags.append(tag_object)

    def __repr__(self) -> str:
        return f'<Image {self.name}>'


class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String, unique=True)

    @classmethod
    def exists(cls, tag_name: str) -> bool:
        return bool(cls.query.filter_by(tag_name=tag_name).scalar())

    def __repr__(self) -> str:
        return f'<Tag {self.tag_name}>'
