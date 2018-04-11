def get_rc(puzzle, i, j):
    x = int(i / 3) * 3
    y = int(j / 3) * 3
    rc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Remove from horizontal
    for h in range(0, 9):
        if puzzle[i][h] in rc:
            rc.remove(puzzle[i][h])
    # Remove from vertical
    for v in range(0, 9):
        if puzzle[v][j] in rc:
            rc.remove(puzzle[v][j])
    # Remove from rectangle
    for rx in range(x, x + 3):
        for ry in range(y, y + 3):
            if puzzle[rx][ry] in rc:
                rc.remove(puzzle[rx][ry])
    return rc[0] if len(rc) == 1 else rc


def naked_single(puzzle):
    find_new = False
    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] == 0 or isinstance(puzzle[i][j], list):
                puzzle[i][j] = get_rc(puzzle, i, j)
                if isinstance(puzzle[i][j], int):
                    find_new = True
    return find_new


def sudoku(puzzle):
    while True:
        if not naked_single(puzzle):
            break
    return puzzle


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

res = sudoku(puzzle)
for row in res:
    for num in row:
        print '%s, ' % str(num),
    print
