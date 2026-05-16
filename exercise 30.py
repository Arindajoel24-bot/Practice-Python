import random

#read the file
with open("words.txt", "r")as file:
    line = file.readlines()
    word = random.choice(line).strip()
    print(word)
