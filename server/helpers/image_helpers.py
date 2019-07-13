from typing import Dict, List

from werkzeug.datastructures import FileStorage


def save_image(uploaded_image: FileStorage, categorised_tags: Dict):

    image_hex_bytes = uploaded_image.read()
    image = _hex_to_image(image_hex_bytes)
    uploaded_image.seek(0)

    exif_data = _format_exif_data(image.getexif())
    updated_categorised_tags = _update_tags_with_exif(exif_data, categorised_tags)
    image_name = _generate_image_name(uploaded_image.filename, exif_data)

    if is_production():
        _save_image_to_s3_bucket(uploaded_image, image_name)
    else:
        _save_image_locally(image, image_name)

    db_image = Image(name=image_name, exif_data=exif_data)
    db_image.add_tags(updated_categorised_tags)

    db.session.add(db_image)
    db.session.commit()


def remove_image(image_id: str) -> None:

    image = Image.query.filter_by(id=image_id).first()

    if is_production():
        _delete_image_in_s3_bucket(image.name)
    else:
        _delete_image_locally(image.name)

    db.session.delete(image)
    db.session.commit()


def load_image(image_name: str) -> str:

    if is_production():
        # return f"https://metuo-server.s3.eu-west-2.amazonaws.com/{image_name}"
        return f"http://d1sq2bjn8ziqtj.cloudfront.net/{image_name}"
    else:
        return url_for("static", filename=image_name, _external=True)


def _generate_image_name(file_name: str, exif_data: Dict) -> str:

    string_to_hash = file_name + exif_data['DateTimeOriginal']
    file_extension = file_name.split('.')[-1]
    file_name_hash = str(uuid.uuid5(uuid.NAMESPACE_DNS, string_to_hash))

    return file_name_hash + '.' + file_extension


def _hex_to_image(image_hex_bytes) -> JpegImageFile:

    image_stream = io.BytesIO(image_hex_bytes)
    image = PILImage.open(image_stream)

    return image


def _format_exif_data(unformatted_exif_data) -> Dict:
    return {
        ExifTags.TAGS[exif_index]: str(exif_data, 'utf-8') if isinstance(exif_data, bytes) else exif_data
        for exif_index, exif_data in unformatted_exif_data.items()
        if exif_index in ExifTags.TAGS
    }
