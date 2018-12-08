class Claim:
    def __init__(self, input):
        claim = input.split()
        self.id = claim[0][1:]
        start = claim[2][:-1].split(",")
        self.startx = int(start[0])
        self.starty = int(start[1])
        size = claim[3].split("x")
        self.x = int(size[0])
        self.y = int(size[1])

    def __str__(self):
        return 'id {}, start {},{}, dimensions {}x{}'.format(self.id,self.startx,self.starty,self.x,self.y)

if __name__ == '__main__':
    claims = list()
    sheet = [[0] * 1000 for i in range(1000)]
    with open('input.txt') as file:
        for line in file:
            claims.append(Claim(line))
    for claim in claims:
        for x in range(claim.x):
            for y in range(claim.y):
                sheet[x+claim.startx][y+claim.starty] += 1
    overlaps = 0
    for x in sheet:
        for y in x:
            if y > 1:
                overlaps += 1
    print(overlaps)

