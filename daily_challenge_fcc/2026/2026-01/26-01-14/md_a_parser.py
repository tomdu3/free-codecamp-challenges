import re

regex = re.compile(r'\[(.*?)\]\((.*?)\)')

def parse_link(md):
    a_elements = re.findall(regex, md)
    return f'<a href="{a_elements[0][1]}">{a_elements[0][0]}</a>'

