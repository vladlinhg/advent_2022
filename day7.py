class Directory:
    def __init__(self, name) -> None:
        self.name = name
        self.upper = None
        self.lower = []
        self.files = []
    
    def set_upper(self, upper):
        self.upper = upper
    
    def get_upper(self):
        return self.upper
    
    def add_lower(self, lower):
        if not lower in self.lower:
            self.lower.append(lower)
    
    def get_lower(self, name):
        for l in self.lower:
            if str(l.name) == str(name):
                return l
    
    def add_file(self, file):
        self.files.append(file)
    
    def get_files(self):
        return self.files
    
def get_total(directory, total):
    total_size = int(total)
    for items in directory.files:
        total_size += items.size
    for item in directory.lower:
        total_size += get_total(item, total_size)
    return total_size

    
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
    




class Command:
    def __init__(self, string):
        string = string.strip()
        self.commands = string.split(" ")
    
    def is_command(self):
        if self.commands[0] == "$":
            return True
        else:
            return False
    
    def is_cd(self):
        if self.commands[1] == "cd":
            return True
        else:
            return False
    
    def cd(self, list, cur: Directory):
        if str(self.commands[2]) in [d.name for d in list]:
            for d in list:
                if str(d.name) == str(self.commands[2]):
                    return d
        else:
            if isinstance(cur, Directory):
                d = Directory(str(self.commands[2]))
                d.set_upper(cur)
                list.append(d)
                return d
            else:
                d = Directory(str(self.commands[2]))
                list.append(d)
                return d

   
    
    def is_upper(self):
        if self.commands[2] == "..":
            return True
        else:
            return False
    def get_upper(self, cur: Directory):
        return cur.get_upper()
        
    
    def is_dir(self):
        if self.commands[0] == "dir":
            return True
        else:
            return False

    def get_dir(self, list, cur: Directory):
        if str(self.commands[1]) not in [d.name for d in list]:
            d = Directory(self.commands[1])
            d.set_upper(cur)
            cur.add_lower(d)
    
    def get_file(self, list, cur: Directory):
        if str(self.commands[1]) not in [f.name for f in list]:
            f = File(self.commands[1], self.commands[0])
            cur.add_file(f)




with open('day7.txt') as f:
    lines = f.readlines()

directories = []
files = []
cur = ""
for line in lines:
    command = Command(line)
    if command.is_command():
        if command.is_cd():
            if command.is_upper():
                cur = command.get_upper(cur)
            else:
                cur = command.cd(directories, cur)
    else:
        if command.is_dir():
            command.get_dir(directories, cur)
        else: 
            command.get_file(files, cur)

total = 0
for d in directories:
    res = get_total(d, 0)
    if res <= 100000:
        total += int(res)

print(total)

for d in directories[:5]:
    print(d.name, d.upper, d.lower, d.files, get_total(d, 0))


