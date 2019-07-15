

def _save_image_file_locally(image: JpegImageFile, image_name: str) -> None:

    image_directory = app.config["IMAGE_DIRECTORY"]
    image_location = os.path.join(image_directory, image_name)

    image.save(image_location)


def _delete_image_file_locally(image_location: str) -> None:
    image_directory = app.config["IMAGE_DIRECTORY"]
    image_location = os.path.join(image_directory, image_location)
    os.remove(image_location)


def _save_image_file_to_s3_bucket(image: FileStorage, image_name: str) -> None:

    image_directory = app.config["IMAGE_DIRECTORY"]

    if is_production():
        s3_client = boto3.client('s3')
    else:
        s3_client = boto3.client('s3',
                                 aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                 aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

    response = s3_client.upload_fileobj(image, image_directory, image_name)

    if response:
        print(response)


def _delete_image_in_s3_bucket(image_name: str) -> None:

    image_directory = app.config["IMAGE_DIRECTORY"]

    if is_production():
        s3_client = boto3.client('s3')
    else:
        s3_client = boto3.client('s3',
                                 aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                 aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

    response = s3_client.delete_object(Bucket=image_directory, Key=image_name)

    if response:
        print(response)
