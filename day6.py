class Pattern:
    def __init__(self, string) -> None:
        s1 = set(string)
        if len(s1) == len(string):
            self.yes = True
        else:
            self.yes = False
        

class New_Pattern:
    def __init__(self, string) -> None:
        s1 = set(string)
        if len(s1) == len(string):
            self.yes = True
        else:
            self.yes = False
    


with open('day6.txt') as f:
    data = f.readline()

number = 0
for i in data:
    pattern = New_Pattern(data[int(number):int(number+14)])
    if pattern.yes:
        print(int(number + 14))
        break
    number += 1
print("Done!")
    

