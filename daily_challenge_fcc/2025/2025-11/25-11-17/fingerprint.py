def is_match(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b):
        return False
    
    differences = sum(1 for a, b in zip(fingerprint_a, fingerprint_b) if a != b)
    
    return not differences > 0.1 * len(fingerprint_a)