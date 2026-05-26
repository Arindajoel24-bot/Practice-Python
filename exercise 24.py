user = int(input("Enter size: "))

horizontal = " ---" * user
row = "|  " * user + "|"

for i in range(user):
    print(horizontal)
    print(row)
print(horizontal)
