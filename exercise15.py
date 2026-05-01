def reversed_string():
    user = input("Enter string: ")

    output = user.split(" ")
    output.reverse()
    output = " ".join(output)
    print(output)

reversed_string()