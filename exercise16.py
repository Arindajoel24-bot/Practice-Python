import random
import string

def main():
    user = input("Do you prefer a weak or strong password: ").title()

    if user == "Weak" :
        words = ["Joel", "Dog", "Strings", "Table", "Food", "Isaac", "Eggs"]
        password = random.choice(words)

        print(password) 
    elif user == "Strong":
        
        length = 12
        b = "".join(random.choice(string.ascii_letters + string.punctuation)for _ in range(length))
        
        print(b)

main()   




    