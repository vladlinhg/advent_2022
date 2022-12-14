import math


class Tree:
    def __init__(self, x, y, h) -> None:
        self.x = int(x)
        self.y = int(y)
        self.h = int(h)
    
    def is_visible(self, trees) -> bool:
        visible = {"l": True, "r": True, "u": True, "d": True}
        
        for tree in trees:
            if tree.x == self.x and tree.y < self.y:
                if tree.h >= self.h:
                    visible["d"] = False
            if tree.x == self.x and tree.y > self.y:
                if tree.h >= self.h:
                    visible["u"] = False
            if tree.y == self.y and tree.x < self.x:
                if tree.h >= self.h:
                    visible["l"] = False
            if tree.y == self.y and tree.x > self.x:
                if tree.h >= self.h:
                    visible["r"] = False
            if visible["l"] == False and visible["r"] == False and visible["u"] == False and visible["d"] == False:
                return False
        return True

    def view_score(self, trees) -> int:
        max_len = int(math.sqrt(len(trees)))-1
        max_score = {"l": self.x, "r": max_len-self.x, "u": max_len-self.y, "d":self.y}
        if self.x == 0:
            return 0
        if self.x == int(math.sqrt(len(trees)))-1:
            return 0
        if self.y == 0:
            return 0
        if self.y == int(math.sqrt(len(trees)))-1:
            return 0
        
        for tree in trees:  
            if tree.x == self.x and tree.y < self.y:
                if tree.h >= self.h:
                    max_distance = abs(tree.y - self.y)
                    max_score["d"] = min(max_score["d"], max_distance)
            if tree.x == self.x and tree.y > self.y:
                if tree.h >= self.h:
                    max_distance = abs(tree.y - self.y)
                    max_score["u"] = min(max_score["u"], max_distance)
            if tree.y == self.y and tree.x < self.x:
                if tree.h >= self.h:
                    max_distance = abs(tree.x - self.x)
                    max_score["l"] = min(max_score["l"], max_distance)
            if tree.y == self.y and tree.x > self.x:
                if tree.h >= self.h:
                    max_distance = abs(tree.x - self.x)
                    max_score["r"] = min(max_score["r"], max_distance)
                    
        return max_score["u"]*max_score["d"]*max_score["l"]*max_score["r"]


with open('day8.txt') as f:
    lines = f.readlines()

forest = []

for i, row in enumerate(lines):
    row = row.strip()
    nums = [row[i:i+1] for i in range(0, len(row), 1)]
    for n, col in enumerate(nums):
        tree = Tree(n, i, col)
        forest.append(tree)

visible = 0

for tree in forest:
    if tree.is_visible(forest):
        visible += 1

print(visible) 


max_d = 0
for tree in forest:
    max_d = max(tree.view_score(forest), max_d)

print(max_d)