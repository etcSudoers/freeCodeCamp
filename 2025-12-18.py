def create_board(dimensions):
    startWith = 0
    rows = dimensions[0]
    col = dimensions[1]
    print(f"rows: {rows}")
    print(f"col:  {col}")
    grid = [["X" if (r + c) % 2 == 0 else "O" for c in range(col) ] for r in range(rows)]
    print(grid)
    
    return grid

assert create_board([3, 3]) ==[["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
assert create_board([6, 1]) ==[["X"], ["O"], ["X"], ["O"], ["X"], ["O"]]
assert create_board([2, 10]) ==[["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]]
assert create_board([5, 4]) ==[["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]]