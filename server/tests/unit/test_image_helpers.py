import os
import copy

import pytest

from server.helpers.image_helpers import load_image, generate_hashed_image_name, _hex_to_image, _format_exif_data


class TestLoadImage:

    def test_load_image_production(self):

        os.environ['PYTHON_ENV'] = 'production'
        image_name = 'test_image.jpg'
        expected_loaded_image_location = f'http://d1sq2bjn8ziqtj.cloudfront.net/{image_name}'

        assert expected_loaded_image_location == load_image(image_name)

    def test_load_image_not_production(self, flask_app):

        os.environ['PYTHON_ENV'] = 'not_production'
        image_name = 'test_image.jpg'
        expected_loaded_image_location = f'http://localhost/static/{image_name}'

        assert expected_loaded_image_location == load_image(image_name)


class TestGenerateImageName:

    def test_generate_image_name(self, valid_exif_dict):

        image_name = 'test_image.jpg'
        expected_generated_image_name = 'e9ca750e-2055-5bc8-9f82-c7dce4f164aa.jpg'

        assert expected_generated_image_name == generate_hashed_image_name(image_name, valid_exif_dict)

    def test_generate_image_name_bad_exif(self, valid_exif_dict):

        image_name = 'test_image.jpg'
        invalid_exif_dict = copy.deepcopy(valid_exif_dict)
        del invalid_exif_dict['DateTimeOriginal']

        with pytest.raises(KeyError):
            generate_hashed_image_name(image_name, invalid_exif_dict)

    def test_generate_image_name_file_name_uniqueness(self, valid_exif_dict):

        image_name_1 = 'test_image_one.jpg'
        image_name_2 = 'test_image_two.jpg'

        generated_name_1 = generate_hashed_image_name(image_name_1, valid_exif_dict)
        generated_name_2 = generate_hashed_image_name(image_name_2, valid_exif_dict)

        assert generated_name_1 != generated_name_2

    def test_generate_image_name_exif_data_uniqueness(self, valid_exif_dict):

        image_name = 'test_image.jpg'

        exif_dict_1 = copy.deepcopy(valid_exif_dict)
        exif_dict_1['DateTimeOriginal'] = '2020:01:26 02:54:31'

        exif_dict_2 = copy.deepcopy(valid_exif_dict)
        exif_dict_2['DateTimeOriginal'] = '2020:01:27 02:54:31'

        generated_name_1 = generate_hashed_image_name(image_name, exif_dict_1)
        generated_name_2 = generate_hashed_image_name(image_name, exif_dict_2)

        assert generated_name_1 != generated_name_2


class TestHexToImage:

    def test_hex_to_image(self):
        pass

    def test_hex_to_image_invalid_hex(self):
        pass


class TestFormatExifData:

    def test_format_exif_data(self):
        pass

    def test_format_exif_data_invalid_exif_data(self):
        pass
