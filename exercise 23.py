with open("23.txt 1", "r")as file1:
    with open("23.txt 2", "r")as file2:
        prime_numbers = file1.readlines()
        funny_numbers = file2.readlines()
        funny_numbers = [n.strip() for n in funny_numbers]
        lapping_numbers = []
        for number in prime_numbers:
            number = number.strip()
            if number in funny_numbers:
                lapping_numbers.append(number)
print(lapping_numbers)
