import os
import io
import uuid
import calendar
from typing import Dict, List

import boto3
from flask import url_for, current_app as app
from PIL import Image as PILImage, ExifTags
from PIL.JpegImagePlugin import JpegImageFile
from werkzeug.datastructures import FileStorage

from server.models import Image, Tag, db


def is_production() -> bool:

    if os.getenv('PYTHON_ENV') == 'production':
        return True
    else:
        return False
