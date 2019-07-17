

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
