class Elf:
    def __init__(self, id, total):
        self.id = id
        self.total = total

with open('day1.txt') as f:
    lines = f.readlines()

elves = []
tmp = 0
id = 1
for line in lines:
    line = line.strip()
    if line:
        tmp += int(line)
        continue
    elf = Elf(id, tmp)
    id += 1
    tmp = 0
    elves.append(elf)
    

max = []
for elf in elves:
    max.append(elf.total)

max = sorted(max)

print(max[-1] + max[-2] + max[-3])
