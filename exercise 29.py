def main():

    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
 
    current_player = "X"

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
            result = check_winner(board)
            if result == "Player X wins":
                print("Player X wins")
                break
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
            result = check_winner(board)
            if result == "Player O wins":
                print("Player O wins")
                break
            current_player = "X"
            for element in board:
                print(" | ".join("_" if x == 0 else str(x) for x in element))
            board_full = True
            for r in board:
                if 0 in r:
                    board_full = False
            if board_full:
                break
              
    
def check_winner(game):
        #checking rows
        if game[0][0] == "X" and game[0][1] == "X" and game[0][2] == "X":
            return "Player X wins"
        elif game[0][0] == "O" and game[0][1] == "O" and game[0][2] == "O":
                return "Player O wins"
        
        if game[1][0] == "X" and game[1][1] == "X" and game[1][2] == "X":
            return "Player X wins"
        elif game[1][0] == "O" and game[1][1] == "O" and game[1][2] == "O":
                return "Player O wins"
        
        if game[2][0] == "X" and game[2][1] == "X" and game[2][2] == "X":
            return "Player X wins"
        elif game[2][0] == "O" and game[2][1] == "O" and game[2][2] == "O":
                return "Player O wins"
        
        #checking columns
        if game[0][0] == "X" and game[1][0] == "X" and game[2][0] == "X":
            return "Player X wins"
        elif game[0][0] == "O" and game[1][0] == "O" and game[2][0] == "O":
            return "Player O wins"
        
        if game[0][1] == "X" and game[1][1] == "X" and game[2][1] == "X":
            return "Player X wins"
        elif game[0][1] == "O" and game[1][1] == "O" and game[2][1] == "O":
            return "Player O wins"
        
        if game[0][2] == "X" and game[1][2] == "X" and game[2][2] == "X":
            return "Player X wins"
        elif game[0][2] == "O" and game[1][2] == "O" and game[2][2] == "O":
            return "Player O wins"
        
        #checking diagonals
        if game[0][0] == "X" and game[1][1] == "X" and game[2][2] == "X":
            return "Player X wins"
        elif game[0][0] == "O" and game[1][1] == "O" and game[2][2] == "O":
            return "Player O wins"
            
        if game[0][2] == "X" and game[1][1] == "X" and game[2][0] == "X":
            return "Player X wins"
        elif game[0][2] == "O" and game[1][1] == "O" and game[2][0] == "O":
            return "Player O wins"
        else:
            return "Drew"
    


if __name__ == "__main__":
    main()