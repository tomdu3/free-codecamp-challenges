def truncate_text(text):
    if len(text) > 20:
        text = text[:17] + "..."

    return text
