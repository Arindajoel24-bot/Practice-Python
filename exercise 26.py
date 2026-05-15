def main():
    game2 = [[2, 2, 2],
            [1, 1, 0],
            [0, 1, 0]]

    
    print(check_winner(game2))
    
def check_winner(game):
        #checking rows
        if game[0][0] == 1 and game[0][1] == 1 and game[0][2] == 1:
            return "Player1 wins"
        elif game[0][0] == 2 and game[0][1] == 2 and game[0][2] == 2:
                return "Player2 wins"
        
        if game[1][0] == 1 and game[1][1] == 1 and game[1][2] == 1:
            return "Player1 wins"
        elif game[1][0] == 2 and game[1][1] == 2 and game[1][2] == 2:
                return "Player2 wins"
        
        if game[2][0] == 1 and game[2][1] == 1 and game[2][2] == 1:
            return "Player1 wins"
        elif game[2][0] == 2 and game[2][1] == 2 and game[2][2] == 2:
                return "Player2 wins"
        
        #checking columns
        if game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1:
            return "Player1 wins"
        elif game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 2:
            return "Player2 wins"
        
        if game[0][1] == 1 and game[1][1] == 1 and game[2][1] == 1:
            return "Player1 wins"
        elif game[0][1] == 2 and game[1][1] == 2 and game[2][1] == 2:
            return "Player2 wins"
        
        if game[0][2] == 1 and game[1][2] == 1 and game[2][2] == 1:
            return "Player1 wins"
        elif game[0][2] == 2 and game[1][2] == 2 and game[2][2] == 2:
            return "Player2 wins"
        
        #checking diagonals
        if game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1:
            return "Player1 wins"
        elif game[0][0] == 2 and game[1][1] == 2 and game[2][2] == 2:
            return "Player2 wins"
            
        if game[0][2] == 1 and game[1][1] == 1 and game[2][0] == 1:
            return "Player1 wins"
        elif game[0][2] == 2 and game[1][1] == 2 and game[2][0] == 2:
            return "Player2 wins"
        return "Drew"
if __name__ == "__main__":
    main()