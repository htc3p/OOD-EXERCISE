# E <value> ใส่ value ใน queue
# D Dequeue ตัวหน้าสุด --> print(q.pop(0))

class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
def check_inp(input):
    if len(input)==1:
        return input
    else:
        height = [e for e in input.split(' ')][1]
        return int(height)
    

q = Queue()
temp = Queue()
inp = input('Enter Input : ').split(',')

for i in inp:
    data = check_inp(i)

    if data == 'D':
        if q.isEmpty():
            print("Empty")
        else:
            if q.size() == 1:
                value = q.dequeue()
                print(value, '<- Empty')
                temp.enqueue(value)
            else:
                value = q.dequeue()
                temp.enqueue(value)
                print(value, '<-', ', '.join(q.items))

    else:
        q.enqueue(str(data))
        print(', '.join(q.items))

if not q.isEmpty():
    if temp.isEmpty():
        print('Empty', ':', ', '.join(q.items))
    else:
        print(', '.join(temp.items), ':', ', '.join(q.items))
else:
    if temp.isEmpty():
        print('Empty', ':', 'Empty')
    else:
        print(', '.join(temp.items), ':', 'Empty')