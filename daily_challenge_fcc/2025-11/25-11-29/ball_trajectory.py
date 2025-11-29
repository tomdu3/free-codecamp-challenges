def get_next_location(matrix):
    """
    Given a matrix with previous (1) and current (2) ball positions,
    calculate the next position of the ball considering bouncing off walls.
    """
    prev = [0, 0]
    curr = [0, 0]
    
    # Find previous (1) and current (2) positions
    for row_idx, row in enumerate(matrix):
        for col_idx, val in enumerate(row):
            if val == 1:
                prev = [row_idx, col_idx]
            elif val == 2:
                curr = [row_idx, col_idx]
    
    # Compute movement vector from prev to curr
    delta_row = curr[0] - prev[0]
    delta_col = curr[1] - prev[1]
    
    max_row = len(matrix)
    max_col = len(matrix[0])
    
    # Calculate next position
    next_row = curr[0] + delta_row
    next_col = curr[1] + delta_col
    
    # Bounce off top/bottom walls
    if next_row < 0 or next_row >= max_row:
        delta_row = -delta_row
        next_row = curr[0] + delta_row
    
    # Bounce off left/right walls
    if next_col < 0 or next_col >= max_col:
        delta_col = -delta_col
        next_col = curr[1] + delta_col
    
    return [next_row, next_col]
