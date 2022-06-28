def find_next(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None
def valid(puzzle, guess, row, col):
    r_valid = puzzle[row]
    if guess in r_valid:
        return False
    c_valid = []
    for i in range(9):
        c_valid.append(puzzle[i][col])
    if guess in c_valid:
        return False
    row_s = (row//3)*3
    col_s = (col//3)*3
    for r in range(row_s,row_s +3):
        for c in range(col_s,col_s+3):
            if puzzle[r][c] == guess:
                return False
def solve(puzzle):
    r, c = find_next(puzzle)

    if r == None:
        return True

    for guess in range(1,10):
        if valid(puzzle, guess, r, c):
            guess = puzzle[r][c]
            if solve(puzzle):
                return True
        puzzle[r][c] = -1
    
    