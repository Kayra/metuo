from api.database import get_db

db = get_db()


class Image(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # location
    exif_data = db.Column(db.JSON)
