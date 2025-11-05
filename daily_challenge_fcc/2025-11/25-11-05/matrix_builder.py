def build_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = [0 for _ in range(cols)]
        matrix.append(row)
    return matrix
