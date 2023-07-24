class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        
    def __str__(self):
        s = 'stack of '+ str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
        return s
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)