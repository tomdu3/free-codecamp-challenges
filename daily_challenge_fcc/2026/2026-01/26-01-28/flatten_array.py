def flatten_array(arr):
    flattened = []
    for item in arr:
        if isinstance(item, list):
            # Recursively flatten the nested list
            flattened.extend(flatten_array(item))
        else:
            # Append the item to the flattened list
            flattened.append(item)
    return flattened
