# แถวหลัก 1แถว ยาวกี่คนก็ได้ 
# แถวหน้า cashier 1 ยาว 5 คน --> ใช้เวลา 3 นาทีในการคิดค่าบริการ
# แถวหน้า cashier 2 ยาว 5 คน --> ใช้เวลา 2 นาทีในการคิดค่าบริการ
# moveแถว ทุก 1 นาที  * แถว 1 เต็ม --> ไปแถว 2


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

# define variables
people, minute = input("Enter people and time : ").split()
minute = int(minute)

# create queues
main = Queue()
q1 = Queue()
q2 = Queue()

# enqueue item in main
for item in people:
    main.enqueue(item)

j=0
for i in range(minute):
    if i>0 and i%3 == 0 and not q1.isEmpty():
        q1.dequeue()
    if j>0 and j%2 == 0 and not q2.isEmpty():
        q2.dequeue()

    if main.size() > 0:
        if q1.size() < 5:
            q1.enqueue(main.dequeue())
        else:
            q2.enqueue(main.dequeue())

            if q2.size()==1:
                j=0
    
    j += 1
    print(f'{i+1} {main.items} {q1.items} {q2.items}')