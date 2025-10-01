from transpose_matrix import rotate

# rotate([[1]]) should return [[1]].
# Failed:2. rotate([[1, 2], [3, 4]]) should return [[3, 1], [4, 2]].
# Failed:3. rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return [[7, 4, 1], [8, 5, 2], [9, 6, 3]].
# Failed:4. rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]) should return [[0, 1, 0], [0, 0, 1], [0, 1, 0]].

def test_rotate():
    assert rotate([[1]]) == [[1]]
    assert rotate([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]) == [[0, 1, 0], [0, 0, 1], [0, 1, 0]]