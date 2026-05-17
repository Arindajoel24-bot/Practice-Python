try:
    birthday = {
        "Joel": "03/03/2006",
        "Joshua": "18/05/2011",
        "Jordan": "24/04/2004",
    }

    user = input("Enter the name: ")

    print(f"{user}'s birthday is {birthday[user]}")
except KeyError:
    print("Name not in a dictionary.")