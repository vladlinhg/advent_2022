class Move:
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)
    
    def follow_head(self, tail):
        if abs(self.x - tail.x) > 1 or abs(self.y - tail.y) > 1:
            if abs(self.x - tail.x) == 2:
                x = int((self.x + tail.x)/2)
                y = self.y
                return Move(x, y)
            if abs(self.y - tail.y) == 2:
                x = self.x
                y = int((self.y + tail.y)/2)
                return Move(x, y)
            else:
                return Move(int((self.x + tail.x + 1)/2), int((self.y + tail.y + 1)/2)) 
        else:
            return Move(tail.x, tail.y)
    def record_step(self):
        return (self.x, self.y)

class Knots:
    def __init__(self, number:int, head:Move) -> None:
        self.number = int(number)
        self.knots = []
        knot = head.follow_head(head)
        for i in range(number):
            knot = head.follow_head(knot)
            self.knots.append(knot)
            head = knot
    
    def move_head(self, head:Move):
        for i, knot in enumerate(self.knots):
            knot = head.follow_head(knot)
            self.knots[i] = knot
            head = knot
    
    def record_last(self):
        return (self.knots[8].x, self.knots[8].y)

with open('day9.txt') as f:
    lines = f.readlines()

steps = []
cur = {"x":int(0), "y":int(0)}
head = Move(cur["x"], cur["y"])
tail = Knots(9, head)
tail.move_head(head)
step = tail.record_last()
steps.append(step)

for line in lines:
    line = line.strip().split()
    if line[0].strip() == 'U':
        for n in range(int(line[1].strip())):
            cur['y'] += 1
            head = Move(cur["x"], cur["y"])
            tail.move_head(head)
            step = tail.record_last()
            steps.append(step)
    if line[0].strip() == 'D':
        for n in range(int(line[1].strip())):
            cur['y'] -= 1
            head = Move(cur["x"], cur["y"])
            tail.move_head(head)
            step = tail.record_last()
            steps.append(step)
    if line[0].strip() == 'R':
        for n in range(int(line[1].strip())):
            cur['x'] += 1
            head = Move(cur["x"], cur["y"])
            tail.move_head(head)
            step = tail.record_last()
            steps.append(step)
    if line[0].strip() == 'L':
        for n in range(int(line[1].strip())):
            cur['x'] -= 1
            head = Move(cur["x"], cur["y"])
            tail.move_head(head)
            step = tail.record_last()
            steps.append(step)
print(steps)
steps = set(steps)
print(len(steps))

