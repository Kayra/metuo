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
    encoding_process = db.Column(db.String)
    bits_per_sample = db.Column(db.String)
    color_components = db.Column(db.String)
    x_resolution = db.Column(db.String)
    y_resolution = db.Column(db.String)
    software = db.Column(db.String)
    ycbcr_sub_sampling = db.Column(db.String)
    exposure_program = db.Column(db.String)
    created_at = db.Column(db.String)
    maximum_aperture_value = db.Column(db.String)
    metering_mode = db.Column(db.String)