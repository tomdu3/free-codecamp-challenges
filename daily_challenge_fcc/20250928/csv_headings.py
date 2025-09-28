def get_headings(csv):
    return [heading.strip() for heading in csv.split(',')]