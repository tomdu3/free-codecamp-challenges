def rotate(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    new_matrix = [[0]*num_rows for _ in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            new_matrix[j][num_rows - 1 - i] = matrix[i][j]
    return new_matrix