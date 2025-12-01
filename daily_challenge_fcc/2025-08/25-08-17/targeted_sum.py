def find_target(arr, target):
    checked = set()
    for i in range(len(arr)):
        if i in checked:
            continue
        left = arr[i]
        right = target - left
        if right in arr:
            checked.add(arr.index(right))
            if i != arr.index(right):
                return [i, arr.index(right)]
        checked.add(i)
        
    return 'Target not found'
