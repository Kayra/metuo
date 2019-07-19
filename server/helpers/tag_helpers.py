

def build_categorised_tags(tags: List[Tag]) -> Dict:

    categorised_tags = {}

    for tag in tags:

        category = tag.category.name
        if category in categorised_tags.keys():
            categorised_tags[category].append(tag.name)
        else:
            categorised_tags[category] = [tag.name]

    return categorised_tags


def _tags_from_exif(exif_data: Dict) -> Dict:

    full_date = exif_data['DateTimeOriginal']
    date = full_date.split()[0]
    time = full_date.split()[1]

    year = date.split(':')[0]
    month = date.split(':')[1]
    month_string = calendar.month_name[int(month)]
    day = date.split(':')[2]

    tags = {
        'Year': [year],
        'Month': [month_string],
        'Day': [day]
    }

    return tags


def _update_tags_with_exif(exif_data: Dict, categorised_tags: Dict) -> Dict:

    exif_tags = _tags_from_exif(exif_data)

    for category, tags in exif_tags.items():
        if category not in categorised_tags.keys():
            categorised_tags[category] = tags

    return categorised_tags
