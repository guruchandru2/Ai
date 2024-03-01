def is_safe(row, col, board):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, 8)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(row, board):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(row, col, board):
            board[row][col] = 1
            if solve_n_queens(row + 1, board):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        for col in row:
            if col == 0:
                print(".", end=" ")
            else:
                print("Q", end=" ")
        print()

board = [[0 for _ in range(8)] for _ in range(8)]
if solve_n_queens(0, board):
    print_board(board)
else:
    print("No solution exists")
