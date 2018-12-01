if __name__ == '__main__':
    frequency = 0
    with open('input.txt') as file:
        for line in file:
            change = line.strip()
            if change[0] == '+':
                frequency += int(change.strip('+'))
            else:
                frequency -= int(change.strip('-'))
    print(frequency)