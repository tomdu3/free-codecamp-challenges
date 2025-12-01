import re
def strip_tags(html):
    """Remove HTML tags from a string."""
    tag_re = re.compile(r'<[^>]+>')
    html = tag_re.sub('', html)

    return html