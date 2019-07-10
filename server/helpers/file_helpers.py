

def _save_image_file_locally(image: JpegImageFile, image_name: str) -> None:

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_location = os.path.join(image_directory, image_name)

    image.save(image_location)
