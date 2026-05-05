with open("22.txt", "r")as open_file:
    names = open_file.readlines()
    counts = {}
    for name in names:
        name = name.strip()
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
print(counts)
