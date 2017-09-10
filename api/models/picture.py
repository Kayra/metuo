from api.app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)

    make = db.Column(db.String)
    model = db.Column(db.String)
    aperture = db.Column(db.String)
    exposure_time = db.Column(db.String)
    lens_id = db.Column(db.String)
    focal_length = db.Column(db.String)
    flash = db.Column(db.Boolean)
    file_size = db.Column(db.String)
    mime_type = db.Column(db.String)
    image_width = db.Column(db.String)
    image_height = db.Column(db.String)
