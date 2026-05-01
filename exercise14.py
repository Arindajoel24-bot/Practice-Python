def new_list():
    a = [1, 1, 2, 3, 4, 5, 5, 6]

    ab = []

    for number in a:
        if not number in ab:
            ab.append(number)

    print(ab)
new_list()


def new_set():
    a = {1, 1, 2, 3, 4, 5, 5, 6}

    print(a)

new_set()