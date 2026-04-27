ask = input("Do you want to play the game? ")

while ask == "Yes" or ask == "yes":
        
        player1 = input("Play rock paper scissor game: ")
        player2 = input("Play rock paper scissor game: ")

        #rock
        if player1 == "rock" and player2 == "scissors":
            print("Rock beats scissors. Player1 wins")

        elif player1 == "rock" and player2 == "paper":
            print("Paper beats rock. Player2 wins")

        elif player1 == "rock" and player2 == "rock":
            print("its a tie")
        #scissors
        elif player1 == "scissors" and player2 == "rock":
            print("Rock beats scissors. Player2 wins")

        elif player1 == "scissors" and player2 == "paper":
            print("Scissors beat paper. Player1 wins")

        elif player1 == "scissors" and player2 == "scissors":
            print("Its a tie")

        #paper
        elif player1 == "paper" and player2 == "rock":
            print("Paper beats rock. Player1 wins")

        elif player1 == "paper" and player2 == "scissors":
            print("Scissors beat paper. Player2 wins")

        elif player1 == "paper" and player2 == "paper":
            print("its a tie")


        again = input("Contune playing? ")
        if again == "no" or again == "No":
            break

