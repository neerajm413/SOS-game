def sosgame():
    # Asking the players to input number of columns and rows
    rows = int(input("Enter the number of rows(min 3): "))
    columns = int(input("Enter the number of columns(min 3): "))

    # Adding spaces
    board = [[' ' for _ in range(columns)] for _ in range(rows)]

    current_player = "Player 1"
    player1_points = 0
    player2_points = 0

    #Player Switching
    current_player = "Player 2" if current_player == "Player 1" else "Player 1"

    # Game board printing
    while True:
        print("   ", end="")
        for i in range(1, columns + 1):
            print(f"{i:>2}", end=" ")

        print()
        for i, row in enumerate(board, start=1):
            print(f"{i:>2}", " | ".join(row))
            if i < rows:
                print("  " + "---+" * (columns - 1) + "---")

        row = int(input(f"\n{current_player}, enter the row (1-{rows}): ")) - 1
        column = int(input(f"{current_player}, enter the column (1-{columns}): ")) - 1
        letter = input(f"{current_player}, enter your S or O: ").upper()

        if row < 0 or row >= rows or column < 0 or column >= columns:
            print("Error, try again")
            continue

        if board[row][column] != ' ':
            print("Already occupied, choose other space.")
            continue

        board[row][column] = letter

        # Horizontal SOS check
        for i in range(rows):
            for j in range(column - 2):
                if board[i][j] == "S" and board[i][j+1] == 'O' and board[i][j+2] == "S":
                    if current_player == "Player 1":
                        player1_points += 1
                    else:
                        player2_points += 1

        # Vertical SOS check
        for i in range(rows - 2):
            for j in range(column):
                if board[i][j] == "S" and board[i+1][j] == "O" and board[i+2][j] == "S":
                    if current_player == "Player 1":
                        player1_points += 1
                    else:
                        player2_points += 1

        # Diagonally checking SOS
        for i in range(rows - 2):
            for j in range(columns - 2):
                if board[i][j] == "S" and board[i+1][j+1] == "O" and board[i+2][j+2] == "S":
                    if current_player == "Player 1":
                        player1_points += 1
                    else:
                        player2_points += 1

        # Diagonally checking SOS (opposite side)
        for i in range(2, rows):
            for j in range(columns - 2):
                if board[i][j] == "S" and board[i-1][j+1] == "O" and board[i-2][j+2] == "S":
                    if current_player == "Player 1":
                        player1_points += 1
                    else:
                        player2_points += 1

        print(f"\nCurrent score: Player 1 - {player1_points}, Player 2 - {player2_points}")

        # Checking if all the spaces are filled
        if all(cell != ' ' for row in board for cell in row):
            if player1_points > player2_points:
                print(f"\nPlayer 1 wins with {player1_points} points!")
            elif player2_points > player1_points:
                print(f"\nPlayer 2 wins with {player2_points} points!")
            else:
                print("\nIt's a tie!")
            return

sosgame()