def find_word(matrix, word):
    """
    Find the start and end coordinates of a word in a 2D matrix.
    Args:
        matrix (list of list of str): 2D matrix of lowercase letters.
        word (str): The word to find in the matrix.
    Returns:
        list: A list containing the start and end coordinates of the word.
    """
    word = list(word.lower())
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Check rows (left to right and right to left)
    for r in range(rows):
        for c in range(cols - len(word) + 1):
            if matrix[r][c:c + len(word)] == word:
                return [[r, c], [r, c + len(word) - 1]]
            if matrix[r][c:c + len(word)][::-1] == word:
                return [[r, c + len(word) - 1], [r, c]]
    # Check columns (top to bottom and bottom to top)
    for c in range(cols):
        for r in range(rows - len(word) + 1):
            col_segment = [matrix[r + i][c] for i in range(len(word))]
            if col_segment == word:
                return [[r, c], [r + len(word) - 1, c]]
            if col_segment[::-1] == word:
                return [[r + len(word) - 1, c], [r, c]]
    return None