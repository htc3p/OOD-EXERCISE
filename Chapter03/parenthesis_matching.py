# Parenthesis Matching

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

def match(op, cl):
    opens = "{[("
    closes = ")]}"
    return opens.index(op) == closes.index(cl)

def parenMatching(str):
    s = Stack()
    i = 0
    error = 0

    while i<len(str) and error == 0:
        c = str[i]
        if c in '{[(':
            s.push(c)
        else:
            if c in ')]}':
                if s.size()>0:
                    if not match(s.pop(), c):
                        error = 1   # open & close not match
                else:               # empty stack
                    error = 2       # no open paren
        i+=1

    if not s.isEmpty():      # stack not empty
        error = 3            # open paren(s) excesses, no close paren

    return error, c, i, s

str = input("str: ")
err, c, i, s = parenMatching(str)

if err == 1:
    print(str , 'unmatch open-close ')
elif err == 2:
    print(str , 'close paren excess')
elif err == 3:
    print(str , 'open paren(s) excess ', s.size(),': ',end='' )
    for ele in s.items:
        print(ele,sep=' ',end = '')
    print()
else:
    print(str, 'MATCH')