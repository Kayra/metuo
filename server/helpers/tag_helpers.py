import calendar
from datetime import datetime
from typing import Dict, List

from server.models import Tag


def build_categorised_tags(tags: List[Tag]) -> Dict:

    categorised_tags = dict()

    for tag in tags:

        category = tag.category.name
        if category in categorised_tags.keys():
            categorised_tags[category].append(tag.name)
        else:
            categorised_tags[category] = [tag.name]

    return categorised_tags


def update_categorised_tags_with_exif_data(exif_data: Dict, categorised_tags: Dict) -> Dict:

    exif_tags = generate_categorised_tags_from_exif_data(exif_data)

    for category, tags in exif_tags.items():
        if category not in categorised_tags.keys():
            categorised_tags[category] = tags

    return categorised_tags


def generate_categorised_tags_from_exif_data(exif_data: Dict) -> Dict:

    exif_date = exif_data['DateTimeOriginal']
    full_datetime = datetime.strptime(exif_date, '%Y:%m:%d %H:%M:%S')

    month_string = calendar.month_name[int(full_datetime.month)]

    tags = {
        'Year': [str(full_datetime.year)],
        'Month': [month_string],
        'Day': [str(full_datetime.day)]
    }

    return tags
