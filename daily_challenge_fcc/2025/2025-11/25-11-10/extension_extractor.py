def get_extension(filename):
    ext = "ext"
    if "." in filename:
        ext = filename.split(".")[-1]
    return "none" if "." not in filename or ext == "" else ext
