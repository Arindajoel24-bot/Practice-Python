import random

#read the file
with open("words.txt", "r")as file:
    line = file.readlines()
    word = random.choice(line).strip()
    

correct = []
times = 0
guesses = 6 - times
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
        guesses = 6 - times
        print(f"Incorrect, you are left with {guesses} guesses.")
        if times == 6:
            print("Your guessing chances are over")
            print(f"The word was {word}.")
            break
        