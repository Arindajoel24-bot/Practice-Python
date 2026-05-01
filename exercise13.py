def main():
    user = int(input("Enter number of Fibonnac: "))
    Fibonnac(user)


def Fibonnac(n):
    a, b = 1, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


main()