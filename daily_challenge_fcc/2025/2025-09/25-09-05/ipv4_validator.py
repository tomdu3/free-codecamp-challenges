def is_valid_ipv4(ipv4):
    if ipv4.count(".") != 3:
        return False
    elif ipv4.startswith(".") or ipv4.endswith("."):
        return False
    
    for part in ipv4.split("."):
        if not part.isdigit():
            return False
        elif int(part) < 0 or int(part) > 255:
            return False
        elif part.startswith("0") and len(part) > 1:
            return False
    
    return True