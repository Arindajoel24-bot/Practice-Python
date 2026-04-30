def main():
    number = int(input("Enter number: "))
    print(prime_number(number))

    
def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not a prime number."
    else:
        return "Number is a prime number."
main()