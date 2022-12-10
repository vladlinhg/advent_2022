class Compartments:
    def __init__(self, sack1, sack2) -> None:
        for item in sack1:
            for other in sack2:
                if str(item) == str(other):
                    self.item = str(item)
        if self.item.isupper():
            self.order = ord(self.item) - 38
        else:
            self.order = ord(self.item) - 96

class Three_Compartments:
    def __init__(self, sack1, sack2, sack3) -> None:
        self.item = str(list(set.intersection(*map(set,[sack1, sack2, sack3])))[0])
        if self.item.isupper():
            self.order = ord(self.item) - 38
        else:
            self.order = ord(self.item) - 96

    
with open('day3.txt') as f:
    lines = f.readlines()

total = 0
order = 0
group = []
for line in lines:
    order += 1
    group.append(line.strip())
    if order == 3:
        compartment = Three_Compartments(*group)
        total += compartment.order
        order = 0
        group = []

print(total)
