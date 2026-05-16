word = "EVAPORATE"
correct = []
times = 0
while True:
    guess = input("Guess letter: ").upper()

    if guess in correct:
        print("Letter already guessed.")
    elif guess in word:
        correct.append(guess)
        print("Correct.")
        all_guessed = all(letter in correct for letter in word)
        if all_guessed == True:
            print("You win.")
            print(word)
            break
    elif not guess in word:
        times = times + 1
        print("Incorrect.")
        if times == 6:
            print("Your guessing chances are over")
            print(f"The word was {word}.")
            break
        