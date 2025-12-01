import re
def extract_attributes(element):
    
    re_attr = re.compile(r'(\w+)[=](["](.*?)["])')
    attributes = []
    for match in re_attr.finditer(element):
        attr_name = match.group(1)
        attr_value = match.group(3)
        attributes.append((attr_name, attr_value))

    return [f"{name}, {value}" for name, value in attributes] if attributes else []