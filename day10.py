class Cycle:
    def __init__(self, order, value) -> None:
        self.order = int(order)
        self.value = int(value)
    
    def output(self, log):
        log.append((self.order, self.value))
       
    
    def noop(self, log):
        self.order += 1
        self.output(log)
    
    def addx(self, x, log):
        self.order += 1
        self.output(log)
        self.order += 1
        self.value += int(x)
        self.output(log)

with open('day10.txt') as f:
    lines = f.readlines()

log = []
cycle = Cycle(1, 1)

for line in lines:
    line = line.strip().split()
    if line[0].strip() == 'noop':
        cycle.noop(log)
    else:
        cycle.addx(line[1].strip(), log)


res = 0
for i in log:
    if i[0] in (20, 60, 100, 140, 180, 220):
        res += i[0]*i[1]


print(res)

crt = []

for i in log:
    if (i[0]-1)%40 in (i[1]-1,i[1],i[1]+1):
        crt.append("#")
    else:
        crt.append(".")

for i, s in enumerate(crt):
    if i in (40, 80, 120, 160, 200):
        print("\n", end="")
    print(s, end="")
    