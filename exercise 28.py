def main():
    joel = int(input("Enter number: "))
    josh = int(input("Enter number: "))
    jj = int(input("Enter number: "))

    print(largest(joel, josh, jj))

def largest(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z
   

if __name__ == "__main__":
    main()