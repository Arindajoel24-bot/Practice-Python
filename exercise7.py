a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = []
for number in a:
    if number % 2 == 0:
        x.append(number)
print(x)