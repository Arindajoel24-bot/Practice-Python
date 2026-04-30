import random
number = random.randint(1, 9)
number_guess = 0
while True:
    try:
        guess = input("Guess btn 1 _ 9: ")
        raw = int(guess)
        number_guess += 1
        

        if raw == number:
            print("You guessed the right number.")
            break
        elif raw > number:
            print("You guessed too high.")
        elif raw < number:
            print("You guessed too low")
        
        else:
            print("Invalid input")
    except ValueError:
        if guess == "exit":
            print(f"You have guessed {number_guess} times")
            break
