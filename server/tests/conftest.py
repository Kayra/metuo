from typing import Dict

import pytest

from server import create_app


@pytest.fixture()
def flask_app():

    app = create_app()
    app_context = app.test_request_context()
    app_context.push()
    client = app.test_client()

    yield client


@pytest.fixture()
def valid_exif_dict() -> Dict:

    yield {
        "ExifVersion": "0231",
        "ShutterSpeedValue": [
            11643856,
            1000000
        ],
        "ApertureValue": [
            361471,
            100000
        ],
        "DateTimeOriginal": "2020:01:26 02:54:31",
        "DateTimeDigitized": "2020:01:26 02:54:31",
        "ExposureBiasValue": [
            0,
            1
        ],
        "MaxApertureValue": [
            175,
            100
        ],
        "MeteringMode": 6,
        "ColorSpace": 1,
        "Flash": 16,
        "FocalLength": [
            50,
            1
        ],
        "ExposureMode": 1,
        "WhiteBalance": 0,
        "SceneCaptureType": 0,
        "FocalPlaneXResolution": [
            49807360,
            32768
        ],
        "FocalPlaneYResolution": [
            49807360,
            32768
        ],
        "SubsecTimeOriginal": "37",
        "SubsecTimeDigitized": "37",
        "FocalPlaneResolutionUnit": 3,
        "Model": "Canon EOS 6D",
        "Make": "Canon",
        "ExposureTime": [
            1,
            3200
        ],
        "XResolution": [
            240,
            1
        ],
        "YResolution": [
            240,
            1
        ],
        "FNumber": [
            35,
            10
        ],
        "ExposureProgram": 1,
        "CustomRendered": 0,
        "ISOSpeedRatings": 400,
        "ResolutionUnit": 2,
        "BodySerialNumber": "095053000323",
        "LensSpecification": [
            [
                50,
                1
            ],
            [
                50,
                1
            ],
            [
                0,
                0
            ],
            [
                0,
                0
            ]
        ],
        "LensModel": "EF50mm f/1.8 II",
        "LensSerialNumber": "0000000000",
        "Software": "Adobe Photoshop Lightroom Classic 9.3 (Macintosh)",
        "DateTime": "2020:08:19 17:19:22",
        "ExifOffset": 216
    }


@pytest.fixture()
def valid_category_tags() -> Dict:

    yield {
        "Location": [
            "Japan"
        ],
        "City": [
            "Tokyo"
        ],
        "Colour": [
            "White"
        ],
        "People": [
            "Rie"
        ]
    }