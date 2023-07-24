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
    
def is_operator(char):
    return char in "+-*/"

def precedence(char):
    if char in "*/":
        return 2
    elif char in "+-":
        return 1
    return 0

def infix_to_postfix(expression):
    s = Stack()
    postfix = []

    for char in expression:
        if char.isalnum():  # check char is a letter or a digit --> True, False
            postfix.append(char)
        elif char == '(':
            s.push(char)
        elif char == ')':
            while not s.isEmpty() and s.peek() != '(':
                postfix.append(s.pop())
            if not s.isEmpty() and s.peek() == '(':
                s.pop()     # pop '('
        elif is_operator(char):
            while not s.isEmpty() and precedence(s.peek()) >= precedence(char):
                postfix.append(s.pop())
            s.push(char)
        
    while not s.isEmpty():
        postfix.append(s.pop())

    return ''.join(postfix)


infix_expression = input("Infix Expression: ")
postfix_expression = infix_to_postfix(infix_expression)
print(f"Postfix Expression: {postfix_expression}")