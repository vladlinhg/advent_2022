class Item:
    def __init__(self, worry) -> None:
        self.worry = int(worry)
    
    def worry_change(self, instruction):
        if instruction[0] == "*":
            if instruction[1] == "old":
                self.worry *= self.worry
            else:
                self.worry *= int(instruction[1])
        else:
            self.worry += int(instruction[1])

    def worry_test(self, instruction):
        self.worry /= 3
        if self.worry % instruction == 0:
            return True
        else:
            return False 
    def __str__(self) -> str:
        return str(self.worry)


class Monkey:
    def __init__(self, instruction):
        for line in instruction:
            line = line.strip().split()
            for i, word in enumerate(line):
                line[i] = word.strip(":,")
            if line[0] == "Monkey":
                self.id = int(line[1])
            elif line[0] == "Starting":
                self.items = []
                for i in line:
                    if i == "Starting" or i == "items":
                        continue
                    else:
                        self.items.append(Item(int(i)))
            elif line[0] == "Operation":
                if line[5] == 'old':
                    self.op = [line[4], line[5]]
                else:
                    self.op = [line[4], int(line[5])]
            elif line[0] == "Test":
                self.test = int(line[3])
            elif line[0] == "If":
                if line[1] == "true":
                    self.pas = int(line[5])
                else:
                    self.fai = int(line[5])
        self.insp = 0


    def pass_item(self, item, monkey):
        monkey.items.append(item)
        self.items.remove(item)
    
    def play_item(self):
        for i in self.items:
            i.worry_change(self.op)
    
    def test_item(self, monkeys):
        for monkey in monkeys:
            if monkey.id == self.pas:
                pas = monkey
            if monkey.id == self.fai:
                fai = monkey
        for i in self.items:
            if i.worry_test(self.test):
                self.pass_item(i, pas)
            else:
                self.pass_item(i, fai)
            self.insp += 1
    
    def process(self, monkeys):
        self.play_item()
        self.test_item(monkeys)
    
    def print(self):
        print(self.id)
        print(self.items)
        print(self.op)
        print(self.test)
        print(self.pas)
        print(self.fai)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        


with open('day11_t.txt') as f:
    lines = f.readlines()

instructions = []
tmp = []
for line in lines:
    if line == '\n':
          tmp = []
    elif line.strip()[:8] == 'If false':
        tmp.append(line.strip())
        instructions.append(tmp)
    else:
        tmp.append(line.strip())


monkeys = []
for i in instructions:
    monkey = Monkey(i)
    monkeys.append(monkey)

for i in monkeys:
    i.print()

for i in range(20):
    for monkey in monkeys:
        monkey.process(monkeys)

log = []

for monkey in monkeys:
    log.append((monkey.id, monkey.insp))

print(log)
