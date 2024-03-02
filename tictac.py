def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Column win

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Diagonal win

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Diagonal win

    return None  # No winner yet

def is_board_full(board):
    # Check if the board is full (a draw)
    for row in board:
        if ' ' in row:
            return False  # There is an empty space
    return True  # The board is full

def is_valid_move(board, row, col):
    # Check if the move is within the board and the cell is empty
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if is_valid_move(board, row, col):
            board[row][col] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_tic_tac_toe()
