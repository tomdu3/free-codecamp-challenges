def is_sorted(arr: list[int|float]) -> str:
        """Return "Ascending", "Descending", or "Not sorted" if the array is sorted in ascending, descending, or neither order, respectively."""

        if len(arr) <= 1:
            return "Ascending"

        if sorted(arr) == arr:
            return "Ascending"
        elif sorted(arr, reverse=True) == arr:
            return "Descending"
        else:
            return "Not sorted"

if __name__ == '__main__':
    assert is_sorted([1, 2, 3, 4, 5]) == "Ascending"
    assert is_sorted([10, 8, 6, 4, 2]) == "Descending"
    assert is_sorted([1, 3, 2, 4, 5]) == "Not sorted"
    assert is_sorted([3.14, 2.71, 1.61, 0.57]) == "Descending"
    assert is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]) == "Ascending"
    assert is_sorted([0.4, 0.5, 0.3]) == "Not sorted"

