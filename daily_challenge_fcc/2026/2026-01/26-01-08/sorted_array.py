def is_sorted(arr: list[int|float]) -> str:
    """Return "Ascending", "Descending", or "Not sorted" if the array is sorted in ascending, descending, or neither order, respectively."""

    if len(arr) <= 1:
        return "Ascending"

    ascending = True
    descending = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            ascending = False
        elif arr[i] < arr[i + 1]:
            descending = False

    if ascending:
        return "Ascending"
    elif descending:
        return "Descending"
    else:
        return "Not sorted"

if __name__ == '__main__':
    print(is_sorted([1, 2, 3, 4, 5]))
    print(is_sorted([10, 8, 6, 4, 2]))
    print(is_sorted([1, 3, 2, 4, 5]))
    print(is_sorted([3.14, 2.71, 1.61, 0.57]))
    print(is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]))
    print(is_sorted([0.4, 0.5, 0.3]))
