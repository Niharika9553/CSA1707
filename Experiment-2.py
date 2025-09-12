N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, row):
    if row == N:
        print_solution(board)
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack
    return False

board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_n_queens(board, 0):
    print("No solution found.")
