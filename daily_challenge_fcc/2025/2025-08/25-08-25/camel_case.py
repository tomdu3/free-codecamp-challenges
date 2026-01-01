def to_camel_case(s):
    s = s.replace("_", " ").replace("-", " ").split(" ")
    s = [word.capitalize() for word in s if word]
    s[0] = s[0].lower()
    s = "".join(s)

    return s