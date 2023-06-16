def find_blank(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None, None

def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

def is_safe(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    row, col = find_blank(grid)
    if row is None and col is None:
        return True

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

grid = [[0, 4, 8, 0, 0, 0, 0, 7, 0],
        [2, 7, 0, 6, 9, 0, 0, 3, 0],
        [0, 3, 0, 0, 7, 2, 0, 4, 0],
        [3, 0, 0, 0, 0, 0, 4, 1, 0],
        [0, 9, 0, 1, 0, 8, 7, 0, 3],
        [5, 1, 6, 0, 4, 0, 0, 0, 8],
        [0, 2, 0, 0, 0, 9, 1, 0, 0],
        [7, 5, 4, 2, 0, 1, 3, 0, 6],
        [1, 0, 0, 7, 0, 5, 0, 0, 0]]

if solve_sudoku(grid):
    print_grid(grid)
else:
    print("No solution exists")
