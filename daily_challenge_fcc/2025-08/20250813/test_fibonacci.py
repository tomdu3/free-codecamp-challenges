from fibonacci import fibonacci_sequence

def test_fibonacci_20_terms():
    assert fibonacci_sequence([0, 1], 20) == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
        55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
    ]

def test_fibonacci_length_one_returns_first_element():
    assert fibonacci_sequence([21, 32], 1) == [21]

def test_fibonacci_zero_length_returns_empty():
    assert fibonacci_sequence([0, 1], 0) == []

def test_fibonacci_same_length_as_start_sequence():
    assert fibonacci_sequence([10, 20], 2) == [10, 20]

def test_fibonacci_large_numbers():
    assert fibonacci_sequence([123456789, 987654321], 5) == [
        123456789, 987654321, 1111111110, 2098765431, 3209876541
    ]