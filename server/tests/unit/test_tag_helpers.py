from server.helpers.tag_helpers import update_categorised_tags_with_exif_data, \
                                       generate_categorised_tags_from_exif_data


class TestUpdateCategorisedTagsWithExifData:

    def test_update_categorised_tags_with_exif_data(self, valid_exif_dict, valid_category_tags):

        expected_categorised_tags = {
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
            ],
            "Year": [
                "2020"
            ],
            "Month": [
                "January"
            ],
            "Day": [
                "26"
            ]
        }

        actual_categorised_tags = update_categorised_tags_with_exif_data(valid_exif_dict, valid_category_tags)
        
        assert expected_categorised_tags == actual_categorised_tags


class TestGenerateCategorisedTagsFromExifData:

    def test_generate_categorised_tags_from_exif_data(self, valid_exif_dict):
        pass

