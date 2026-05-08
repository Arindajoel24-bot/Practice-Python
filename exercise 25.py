def main():
    low = 0
    high = 100
    number_guess = 0
    while low <= high:
        mid = (low + high)// 2
        print(f"Is it {mid}")
        number_guess += 1
        answer = input("")
        if answer == "yes":
            print(f"I guessed it in {number_guess}")
            break
        if answer == "too high":
            high = mid - 1

        if answer == "too low":
            low = mid + 1
            
if __name__ == "__main__":
    main()