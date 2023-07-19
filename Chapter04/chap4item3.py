# E-Enqueue, D-Dequeue, ตัวอื่น-Error

''' - TEST CASE -
input : D3,E2,E3,D9,E2,ff
Step : D3
Dequeue : []
Error Dequeue : 3
Error input : 0
--------------------
Step : E2
Enqueue : ['*0', '*1']
Error Dequeue : 3
Error input : 0
--------------------
Step : E3
Enqueue : ['*0', '*1', '*2', '*3', '*4']
Error Dequeue : 3
Error input : 0
--------------------
Step : D9
Dequeue : []
Error Dequeue : 7
Error input : 0
--------------------
Step : E2
Enqueue : ['*5', '*6']
Error Dequeue : 7
Error input : 0
--------------------
Step : ff
['*5', '*6']
Error Dequeue : 7
Error input : 1
--------------------
'''

class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


inp = input('input : ').split(',')
q = Queue()

eq_count = 0
error_dequeue = 0
error_input = 0

for n in inp:
    print('Step :', n)
    if n[0] == 'D':
        diff = int(n[1:])-q.size()
        for _ in range(int(n[1:])):
            item = q.dequeue()
            if item is None:
                pass
        
        error_dequeue += diff
        print("Dequeue :", q.items)

    elif n[0] == 'E':
        for _ in range(int(n[1:])):
            item = '*' + str(eq_count)
            q.enqueue(item)
            eq_count += 1

        print("Enqueue :", q.items)

    else:
        error_input += 1
        print(q.items)

    print("Error Dequeue :", error_dequeue)
    print("Error input :", error_input)
    print("--------------------")