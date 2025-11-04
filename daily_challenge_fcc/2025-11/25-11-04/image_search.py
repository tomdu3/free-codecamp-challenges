def image_search(images, term):
    term_lower = term.lower()
    images = [img for img in images if term_lower in img.lower()]
    return images