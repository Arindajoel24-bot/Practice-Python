def main():

    my_list = [1, 3, 5, 7, 9, 11]
    print(binary_search(my_list, 7))

def binary_search(ordered_list, number):
    low = 0
    high = len(ordered_list) - 1

    while low <= high:
        mid = (low + high)// 2           # how do you find the middle index?
        if ordered_list[mid] == number:
            return True
        elif number < ordered_list[mid]:
            high = mid - 1         # search left half
        else:
            low = mid + 1          # search right half

    return False              # number not found

main()