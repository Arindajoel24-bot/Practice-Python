number = [1, 2, 3, 4, 5]
user_number = int(input("Enter number: "))
new_list =[x for x in number if x < user_number]
print(new_list)