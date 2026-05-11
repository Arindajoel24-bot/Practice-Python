current_player = "X"
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
while True:
    if current_player == "X":
        user = input("Enter row, column: ")
        seperate = user.split(",")
        row = int(seperate[0]) - 1
        col = int(seperate[1]) - 1
        if board[row][col] != 0:
            print("Cell already taken")
            continue
        board[row][col] = "X"
        current_player = "O"
        for element in board:
            print(" | ".join("_" if x == 0 else str(x) for x in element))
        board_full = True
        for r in board:
            if 0 in r:
                board_full = False
        if board_full:
            break
    elif current_player == "O":
        user = input("Enter row, column: ")
        seperate = user.split(",")
        row = int(seperate[0]) - 1
        col = int(seperate[1]) - 1
        if board[row][col] != 0:
            print("Cell already taken")
            continue
        board[row][col] = "O"
        current_player = "X"
        for element in board:
            print(" | ".join("_" if x == 0 else str(x) for x in element))
        board_full = True
        for r in board:
            if 0 in r:
                board_full = False
        if board_full:
            break
