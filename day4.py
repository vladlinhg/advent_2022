class Assignment:
    def __init__(self, string):
        strings = string.strip().split(",")
        s1 = strings[0].split("-")
        s2 = strings[1].split("-")
        self.s1 = list(range(int(s1[0]), int(s1[1]) + 1))
        self.s2 = list(range(int(s2[0]), int(s2[1]) + 1))
    
    def is_contain(self):
        if len(self.s1) > len(self.s2):
            for i in self.s2: 
                if i not in self.s1: 
                    return False 
            return True
        else:
            for i in self.s1: 
                if i not in self.s2: 
                    return False 
            return True
    def is_overlap(self):
        for i in self.s1:
            if i in self.s2:
                return True
        return False

with open('day4.txt') as f:
    lines = f.readlines()

total = 0
for line in lines:
    assignment = Assignment(line)
    if assignment.is_overlap():
        total += 1
print(total)