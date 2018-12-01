if __name__ == '__main__':
    frequency = 0
    frequencies = list()
    found = False
    while not found:
        with open('input.txt') as file:
            for line in file:
                change = line.strip()
                if change[0] == '+':
                    frequency += int(change.strip('+'))
                else:
                    frequency -= int(change.strip('-'))
                if frequency in frequencies:
                    print('duplicate frequency: ' + str(frequency))
                    found = True
                    break
                else:
                    #print(frequency)
                    frequencies.append(frequency)