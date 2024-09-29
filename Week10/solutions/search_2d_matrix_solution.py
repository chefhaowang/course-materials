def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False

    # Number of rows and columns
    ROWS, COLS = len(matrix), len(matrix[0])

    # Binary search on a virtual 1D array
    left, right = 0, ROWS * COLS - 1

    while left <= right:
        mid = (left + right) // 2
        
        row = mid // COLS
        col = mid % COLS

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(searchMatrix([[4, 6, 9, 12], [12, 18, 22, 29], [49, 64, 92, 98]], 39))
