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

    def bored(self):
        self.worry = self.worry//int(3)
    
    def worry_test(self, instruction):
        if int(self.worry) % int(instruction) == 0:
            return True
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
    def print_items(self):
        for i in self.items:
            print(i, end=" ")
        print("")
    
    def play_item(self):
        for i in self.items:
            self.insp += 1
            i.worry_change(self.op)
            #print(i)
    
    def test_item(self, monkeys):
        for monkey in monkeys:
            if monkey.id == self.pas:
                pas = monkey
            if monkey.id == self.fai:
                fai = monkey
        #print(pas)
        #print(fai)
        #self.print_items()
        items = [i for i in self.items]

        for i in items:
            #i.bored()

            #print(i)
        
            if i.worry_test(self.test):
                self.pass_item(i, pas)
            else:
                self.pass_item(i, fai)
        
        #print("all items processed")
        
    
    def process(self, monkeys):
        self.play_item()
        self.test_item(monkeys)
    
    def print(self):
        print(self.id)
        self.print_items() 
        print(self.op)
        print(self.test)
        print(self.pas)
        print(self.fai)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    
    def __str__(self) -> str:
        return str(self.id)

        


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

for i in range(1000):
    for monkey in monkeys:
        monkey.process(monkeys)
"""
for i in monkeys:
    i.print()
"""

log = []

for monkey in monkeys:
    log.append((monkey.id, monkey.insp))

print(log)
