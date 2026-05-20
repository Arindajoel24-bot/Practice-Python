import json

#user = input("Enter name and birthday: ")
try: 
    with open("34.json", "r") as file:
        birthdays = json.load(file)
   
    users = input("Enter the name: ")

    print(f"{users}'s birthday is {birthdays[users]}")
except KeyError:
    print("Name not in a dictionary.")
        
user = input("Enter name and birthday: ")   

name, date = user.split(": ")

birthdays[name] = date
print(birthdays)

with open("34.json", "w") as f:
    names = json.dump(birthdays, f, indent=2)

