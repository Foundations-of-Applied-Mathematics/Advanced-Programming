import time

# Given a spot row and column on the board, and a digit to place, will it be valid?
def can_place(board, r, c, digit):
    if digit in board[r] or digit in [board[i][c] for i in range(len(board))]:
        # digit is in a row or column, so nope

        return False

    # Check the 9 squares in the zone of (r, c)
    r_zone = [(r // 3) * 3, (r // 3) * 3 + 1, (r // 3) * 3 + 2]
    c_zone = [(c // 3) * 3, (c // 3) * 3 + 1, (c // 3) * 3 + 2]
    for nr in r_zone:
        for nc in c_zone:
            if board[nr][nc] == digit:
                return False

    return True

'''
def solve(board, r, c):
    if r == len(board):
        return board

    next_r = r + 1 if c == len(board) - 1 else r
    next_c = 0 if c == len(board) - 1 else c + 1

    if board[r][c] == -1:
        for digit in range(1, 10):
            if can_place(board, r, c, digit):
                board[r][c] = digit
                if solve(board, next_r, next_c):
                    return board
                else:
                    board[r][c] = -1
                    '''
def solve_sudoku(board, r, c):
    if r == len(board):
        # If we've reached the end, there are no more solutions to find
        for p in board:
            print(*p)
        return 1

    # calculate next position
    next_r = r + 1 if c == len(board[0]) - 1 else r
    next_c = 0 if c == len(board[0]) - 1 else c + 1

    if board[r][c] == -1:
        solutions = 0
        for k in range(1, 10):
            if can_place(board, r, c, k):
                board[r][c] = k
                solutions += solve_sudoku(board, next_r, next_c)
                board[r][c] = -1
        return solutions
    else:
        return solve_sudoku(board, next_r, next_c)

def sudoku_solver(board):
    return solve_sudoku(board, 0, 0)


if __name__ == "__main__":
    START = time.time()
    test_board = [[-1, -1, -1, 6, 5, -1, -1, -1, 1],
                  [-1, -1, -1, 4, -1, 8, -1, -1, 6],
                  [-1, 3, -1, -1, -1, 7, -1, 8, -1],
                  [9, -1, -1, -1, -1, 1, -1, -1, 3],
                  [-1, 6, -1, -1, 4, -1, -1, 7, -1],
                  [1, -1, -1, 8, -1, -1, -1, -1, 4],
                  [-1, 5, -1, 1, -1, -1, -1, 9, -1],
                  [8, -1, -1, 3, -1, 2, -1, -1, -1],
                  [6, -1, -1, -1, 9, 5, -1, -1, -1]];

    test_board2 = [[-1, 8, -1, -1, -1, -1, 2, -1, -1],
                   [-1, -1, -1, -1, 8, 4, -1, 9, -1],
                   [-1, -1, 6, 3, 2, -1, -1, 1, -1],
                   [-1, 9, 7, -1, -1, -1, -1, 8, -1],
                   [8, -1, -1, 9, -1, 3, -1, -1, 2],
                   [-1, 1, -1, -1, -1, -1, 9, 5, -1],
                   [-1, 7, -1, -1, 4, 5, 8, -1, -1],
                   [-1, 3, -1, 7, 1, -1, -1, -1, -1],
                   [-1, -1, 8, -1, -1, -1, -1, 4, -1]]
    print(sudoku_solver(test_board))
    print(sudoku_solver(test_board2))
    print("ELAPSED TIME: ", time.time() - START)


