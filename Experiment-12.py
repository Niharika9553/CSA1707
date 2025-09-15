# tic_tac_toe.py

def print_board(board):
    """Display the Tic Tac Toe board."""
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(board, player):
    """Check if the current player has won."""
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # row
            return True
        if all(board[j][i] == player for j in range(3)):  # column
            return True
    if all(board[i][i] == player for i in range(3)):  # main diagonal
        return True
    if all(board[i][2-i] == player for i in range(3)):  # anti-diagonal
        return True
    return False

def is_full(board):
    """Check if board is full (draw)."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, enter your move (row and column 1-3):")
        
        try:
            row = int(input("Row: ")) - 1
            col = int(input("Col: ")) - 1
        except ValueError:
            print("❌ Invalid input! Enter numbers between 1 and 3.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = current_player

                if check_winner(board, current_player):
                    print_board(board)
                    print(f"🎉 Player {current_player} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("🤝 It's a draw!")
                    break

                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("❌ That spot is already taken. Try again.")
        else:
            print("❌ Invalid position! Row & Column must be between 1 and 3.")

if __name__ == "__main__":
    play_game()
