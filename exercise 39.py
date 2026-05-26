from datetime import datetime

name = input("What is your name? ")
age = int(input("How old are you? "))

year =  datetime.now().year - age + 100

print(f"{name}: you will be 100 in {year}")