user_input = int(input("Choose the divider: "))

listRange = list(range(1,user_input+1))

dividorlist = []

for number in listRange:
    if user_input % number == 0:
        dividorlist.append(number)
print(dividorlist)