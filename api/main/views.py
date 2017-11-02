
def allowed_image(image_name):

    try:
        image_extension = image_name.rsplit(".", 1)[1].lower()
    except IndexError:
        return False

    return image_extension in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
def upload_image():

    # Read exif data

    if "file" not in request.files:
        return "No image found"

    image = request.files["file"]

    if image.filename == "":
        return "No image or image name"

    if image and allowed_image(image.filename):

        image_name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))
        return "Image uploaded"