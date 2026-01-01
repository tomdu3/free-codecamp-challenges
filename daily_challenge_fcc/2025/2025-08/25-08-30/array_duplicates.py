def find_duplicates(arr):
    seen = []
    duplicates = []
    for el in arr:
        if el not in seen:
            seen.append(el)
        else:
            if el not in duplicates:
                duplicates.append(el)
    return sorted(duplicates)
    
