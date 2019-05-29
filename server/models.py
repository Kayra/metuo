from typing import Dict, List

from server import db


association_table = db.Table('image_tag_association',
                             db.Column('image_id', db.Integer, db.ForeignKey('images.id'), primary_key=True),
                             db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True))


flatten = lambda list_to_flatten: [item for sublist in list_to_flatten for item in sublist]


class Image(db.Model):

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    exif_data = db.Column(db.JSON)

    tags = db.relationship('Tag', secondary=association_table, lazy='subquery',
                           backref=db.backref('images', lazy=True), cascade="all, delete-orphan", single_parent=True)

    def add_tags(self, category_tags: Dict) -> None:

        for category, tags in category_tags.items():

            category_object = Category.get_or_create(category)

            for tag in tags:
                if tag not in [tag.name for tag in self.tags]:
                    tag_object = Tag.get_or_create(tag)
                    tag_object.category = category_object
                    self.tags.append(tag_object)

    def update_tags(self, category_tags_to_update: Dict) -> None:

        tags_to_remove = []

        for current_tag in self.tags:

            if current_tag.name not in flatten(category_tags_to_update.values()):
                tags_to_remove.append(current_tag)

            elif current_tag.category not in category_tags_to_update.keys():
                tags_to_remove.append(current_tag)

        [self.tags.remove(tag_to_remove) for tag_to_remove in tags_to_remove]

        self.add_tags(category_tags_to_update)

        db.session.add(self)
        db.session.commit()

    def to_json(self) -> Dict:
        from server.helpers import build_categorised_tags, load_image
        return {
            self.id: {
                'name': self.name,
                'exif': self.exif_data,
                "categorised_tags": build_categorised_tags(self.tags),
                "location": load_image(self.name)
            }
        }

    def __repr__(self) -> str:
        return f'<Image {self.name}>'


class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    @classmethod
    def exists(cls, name: str) -> bool:
        return bool(cls.query.filter_by(name=name).scalar())

    @classmethod
    def get_or_create(cls, name: str) -> bool:
        return cls.query.filter_by(name=name).one() if cls.exists(name=name) else cls(name=name)

    @classmethod
    def get_images(cls, tags: List[str]) -> List[Image]:

        db_tag_objects = cls.query.filter(cls.name.in_(tags)).all()
        all_images = flatten([tag.images for tag in db_tag_objects])

        images = []

        for image in all_images:
            tag_names = [tag.name for tag in image.tags]
            if all([tag in tag_names for tag in tags]):
                images.append(image)

        return images

    def __repr__(self) -> str:
        return f'<Tag {self.name}>'


class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    tags = db.relationship('Tag', backref='category', lazy=True)

    @classmethod
    def exists(cls, name: str) -> bool:
        return bool(cls.query.filter_by(name=name).scalar())

    @classmethod
    def get_or_create(cls, name: str) -> bool:
        return cls.query.filter_by(name=name).one() if cls.exists(name=name) else cls(name=name)

    def __repr__(self) -> str:
        return f'<Category {self.name}>'
