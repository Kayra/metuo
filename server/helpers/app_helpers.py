import os
from datetime import datetime


def is_production() -> bool:
    return os.getenv('PYTHON_ENV') == 'production'

def get_exif_datetime(exif_data):

    potential_keys = ['DateTimeOriginal', 'DateTime']
    for potential_key in potential_keys:
        if potential_key in exif_data:
            return exif_data[potential_key]
    
    return str(datetime.now())
