import re
def parse_image(markdown):
    img_elements = re.search(r"!\[(.*?)\]\((.*?)\)", markdown)
    
    return f'<img src="{img_elements.group(2)}" alt="{img_elements.group(1)}">'
