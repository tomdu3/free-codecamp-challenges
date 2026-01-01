def find_landing_spot(matrix):
    rows = len(matrix)  # number of rows
    cols = len(matrix[0])  # number of columns
    
    safest_spot = None
    min_danger = float('inf')
    
    # possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(rows):
        for j in range(cols):
            # Only consider cells that are potential landing spots (value 0)
            if matrix[i][j] == 0:
                total_danger = 0
                
                # Check all four neighbours
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    
                    # neigbour within bounds
                    if 0 <= ni < rows and 0 <= nj < cols:
                        total_danger += matrix[ni][nj]
                
                # Update safest spot if the new one is better
                if total_danger < min_danger:
                    min_danger = total_danger
                    safest_spot = [i, j]
    
    return safest_spot