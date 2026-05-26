def main():
    user = int(input("Enter size: "))
    make(user)
def make(u):
    horizontal = " ---" * u
    row = "|  " * u + "|"

    for i in range(u):
        print(horizontal)
        print(row)
    print(horizontal)
if __name__ == "__main__":
    main()