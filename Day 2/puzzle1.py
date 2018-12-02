if __name__ == '__main__':
    twos = 0
    threes = 0
    with open('input.txt') as file:
        for line in file:
            box = line.strip()
            counts = list()
            for letter in box:
                counts.append(box.count(letter))
            if 2 in counts:
                twos += 1
            if 3 in counts:
                threes += 1
    checksum = twos * threes
    print(checksum)
