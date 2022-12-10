class Shape:
    def __init__(self, shape):
        dict = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
        self.shape = int(dict[shape])
        
    def score(self, shape):
        res = self.shape - shape
        if res == 0:
            return self.shape + 3
        if res == 1 or res == -2:
            return self.shape + 6
        if res == -1 or res == 2:
            return self.shape + 0
    
    def plan_score(self, shape):
        res = 0
        if self.shape == 1:
            if shape != 1:
                self.shape = shape - 1
                return res + self.shape
            else:
                self.shape = shape + 2
                return res + self.shape
        if self.shape == 2:
            res += 3
            self.shape = shape
            return res + self.shape
        if self.shape == 3:
            res += 6
            if shape != 3:
                self.shape = shape + 1
                return res + self.shape
            else:
                self.shape = shape - 2
                return res + self.shape


        


with open('day2.txt') as f:
    lines = f.readlines()

total = 0
for line in lines:
    shapes = line.strip().split(" ")
    rival = Shape(shapes[0])
    player = Shape(shapes[1])

    res = player.plan_score(rival.shape)
    total += res

print(total)