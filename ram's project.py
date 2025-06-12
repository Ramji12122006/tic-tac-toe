# Tic Tac Toe Game in Python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # anti-diagonal
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("Invalid input! Enter numbers between 0 and 2.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = current_player
                print_board(board)

                if check_winner(board, current_player):
                    print(f"Player {current_player} wins!")
                    break
                elif is_draw(board):
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Cell already taken! Choose another.")
        else:
            print("Invalid row or column. Please enter 0, 1, or 2.")

# Run the game
tic_tac_toe()
