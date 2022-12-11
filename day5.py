class Stack:
    def __init__(self, list):
        self.cargo = list
    
    def add_cargo(self, cargo):
        self.cargo.append(cargo)
    
    def remove_cargo(self):
        self.cargo.pop()
    
    def add_cargos(self, cargos):
        self.cargo.extend(cargos)
    
    def remove_cargos(self, number):
        self.cargo = self.cargo[:int(0-number)]
    

class Crane:
    def __init__(self, list):
        self.stack = list
    
    def move(self, string):
        step = string.split(" ")
        for move in range(int(step[1].strip())):
            self.stack[int(step[5].strip())-1].add_cargo(str(self.stack[int(step[3].strip())-1].cargo[-1]))
            self.stack[int(step[3].strip())-1].remove_cargo()
    
    def print_final(self):
        final = []
        for s in self.stack:
            final.append(s.cargo[-1])
        print(final)
    
    def move_new(self, string):
        step = string.split(" ")
        self.stack[int(step[5].strip())-1].add_cargos(self.stack[int(step[3].strip())-1].cargo[int(0-int(step[1].strip())):])
        self.stack[int(step[3].strip())-1].remove_cargos(int(step[1].strip()))



stack1 = Stack(['B', 'S', 'V', 'Z', 'G', 'P', 'W'])
stack2 = Stack(['J', 'V', 'B', 'C', 'Z', 'F'])
stack3 = Stack(['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'])
stack4 = Stack(['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'])
stack5 = Stack(['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'])
stack6 = Stack(['G', 'F', 'Q', 'T', 'S', 'L', 'B'])
stack7 = Stack(['L', 'G', 'C', 'Z', 'V'])
stack8 = Stack(['N', 'L', 'G'])
stack9 = Stack(['J', 'F', 'H', 'C'])


crane = Crane([stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9])


with open('day5.txt') as f:
    lines = f.readlines()

for line in lines:
    crane.move_new(line.strip())
crane.print_final()
