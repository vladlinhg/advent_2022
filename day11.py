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
            self.worry += instruction[0]

    def worry_test(self, instruction):
        self.worry /= 3
        if self.worry % instruction == 0:
            return True
        else:
            return False 


class Monkey:
    def __init__(self, instruction):
        self.id = int(instruction["id"])
        self.op = instruction["op"]
        self.test = instruction["test"]
        self.pas = instruction["pas"]
        self.fai = instruction["fai"]
        self.items = instruction["items"]
        self.insp = 0


    def pass_item(self, item, monkey):
        monkey.items.append(item)
        self.items.remove(item)
    
    def play_item(self):
        for i in self.items:
            i.worry_change(self.op)
    
    def test_item(self):
        for i in self.items:
            if i.worry_test(self.test):
                self.pass_item(i, Monkey.objects.get(id=self.pas))
            else:
                self.pass_item(i, Monkey.objects.get(id=self.fai))