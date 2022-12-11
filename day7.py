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
        self.lower.append(lower)
    
    def get_lower(self, name):
        for l in self.lower:
            if str(l.name) == str(name):
                return l
    
    def add_file(self, file):
        self.files.append(file)
    
    def get_files(self):
        return self.files
    
    def get_total(self):
        total = 0
        for f in self.files:
            total += f.size
        if len(self.lower) >= 1:
            for l in self.lower:
                total += l.get_total()
        return total

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    




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
    
    def cd(self, list):
        for d in list:
            if str(d.name) == str(self.commands[2]):
                return d
    
    def is_upper(self):
        if self.commands[1] == "..":
            return True
        else:
            return False
    def get_upper(self, cur):
        return cur.get_upper()
        
    
    def is_dir(self):
        if self.commands[0] == "dir":
            return True
        else:
            return False

    def get_dir(self):
        return Directory(self.commands[1])
    
    def get_file(self):
        return File(self.commands[1], self.commands[0])




with open('day7.txt') as f:
    lines = f.readlines()

directories = []
cur = ""
for line in lines:
    command = Command(line)
    if command.is_command():
        if command.is_cd():
            command.cd(directories)
    if

