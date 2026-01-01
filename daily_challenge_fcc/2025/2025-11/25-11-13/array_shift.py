def shift_array(arr, n):
    """
    Shift an array by n positions with wrapping.
    Given an array and an integer representing how many positions to shift,
    return the shifted array. Positive integers shift left, negative integers
    shift right, and the shift wraps around the array.
    Args:
        arr (list): The input array to be shifted.
        n (int): The number of positions to shift. Positive values shift left,
                 negative values shift right.
    Returns:
        list: The shifted array with wrapping applied.
    Examples:
        >>> shift_array([1, 2, 3], 1)
        [2, 3, 1]
        >>> shift_array([1, 2, 3], -1)
        [3, 1, 2]
        >>> shift_array([1, 2, 3], 3)
        [1, 2, 3]
    """
    if not arr:
        return arr  # Return empty array as is
    if n > 0:
        n = n % len(arr)  # Normalize n to avoid unnecessary full rotations
        arr = arr[n:] + arr[:n]
    elif n < 0:
        n = abs(n) % len(arr)  # Normalize n to avoid unnecessary full rotations
        arr = arr[-n:] + arr[:-n]

    return arr