class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, i):
        self.list.append(i)

    def pop(self):
        while len(self.list)>0:
            self.list.pop()

    def isEmpty(self):
        if len(self.list) <= 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.list)
    
    def __items(self):
        return self.list
    
    @property
    def items(self):
        return self.__items()
    

print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()
for e in ls:
    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():
    s.pop()

print(s.size(),"Data in stack : ",s.items)