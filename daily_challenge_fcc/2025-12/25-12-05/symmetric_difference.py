def difference(arr1, arr2):
    not_in_both = []
    for i in range(max(len(arr1), len(arr2))):
        if i < len(arr1):
            if not arr1[i] in arr2:
                not_in_both.append(arr1[i])
        if i < len(arr2):
            if not arr2[i] in arr1:
                not_in_both.append(arr2[i])
    return not_in_both