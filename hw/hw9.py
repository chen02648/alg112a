#八皇后问题

def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        return True

    solution_found = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            solution_found = solve_n_queens_util(board, row + 1, n) or solution_found

            board[row][col] = 0

    return solution_found

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("无解")
        return

    for row in board:
        print(" ".join(["Q" if col == 1 else "." for col in row]))
    print()

solve_n_queens(8)
