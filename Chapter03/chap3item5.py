# โดนผลกระทบจากเห็ดพิษ 
# เลขคี่ ความสูงเพิ่ม 2 เมตร
# เลขคู่ ความสูงลด 1 เมตร

class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def check_tree_or_look(input):
    if len(input)==1:
        return input
    else:
        height = [e for e in input.split(' ')][1]
        return int(height)

S = Stack()
inp = input('Enter Input : ').split(',')

for i in inp:
    data = check_tree_or_look(i)

    if data == 'B':
        temp = Stack()
        if S.isEmpty():
            num_of_trees = 0
        else:
            max = S.pop()
            temp.push(max)
            num_of_trees = 1

        while (not S.isEmpty()):
            value = S.pop()
            temp.push(value)

            if max < value:
                max = value
                num_of_trees += 1
        
        while (not temp.isEmpty()):
            S.push(temp.pop())
            
        print(num_of_trees)

    elif data == 'S':
        temp2 = Stack()

        if S.isEmpty():
            num_of_trees = 0

        while (not S.isEmpty()):
            value2 = S.pop()
            if value2%2 == 0:
                new_value = value2-1
                temp2.push(new_value)
            else:
                new_value = value2+2
                temp2.push(new_value)

        while (not temp2.isEmpty()):
            S.push(temp2.pop())

    else:
        S.push(data)