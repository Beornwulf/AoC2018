if __name__ == '__main__':
    ids = list()
    with open('input.txt') as file:
        for line in file:
            ids.append(line.strip())
    for i in range(len(ids[0])):
        blankids = list()
        for id in ids:
            id = id[:i] + '-' + id[i+1:]
            if id in blankids:
                print(id.replace('-', ''))
                break
            else:
                blankids.append(id)
