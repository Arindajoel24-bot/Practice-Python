import random
number = random.randint(1, 9)
number_guess = 0
while True:
    try:
        guess = input("Guess btn 1 _ 9: ")
        raw = int(guess)
        if raw >= 10:
            print("The number is out of range.")
            continue
        if raw < 1:
            print("The number should be 1 _ 9.")
            continue
        
        if raw == number:
            number_guess += 1
            print("You guessed the right number.")
            print(f"You have guessed {number_guess} times")
            break
        elif raw > number:
            print("You guessed too high.")
            number_guess += 1
        elif raw < number:
            number_guess += 1
            print("You guessed too low")
        
        else:
            print(f"Invalid Input.")
    except ValueError:
        if guess == "exit":
            print(f"You have guessed {number_guess} times")
            break