import random
number_guess = 0
numbers = str(random.randint(1000, 9999))

while True:
    Cow = 0
    Bull = 0
    guess = input("Enter numbers: ")
    number_guess += 1
    for i, number in enumerate(guess):
        if number == numbers[i]:
            Cow += 1
    
        elif number in numbers:
            Bull += 1    
    print(f"{Cow} cows")
    print(f"{Bull} bulls")
    if Cow == 4:
        print("You 4 cows")
        print(f"You have guesses {number_guess} times")
        break
        
    elif Bull == 4:
        continue
