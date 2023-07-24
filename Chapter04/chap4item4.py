# ร้านกาแฟ เวลาเข้าร้าน-si, เวลาชงกาแฟ-pi
'''TEST CASE
 ***Cafe***
Log : 0,3/0,7/2,3/7,7/10,5/10,1
Time 3 customer 1 get coffee  
Time 6 customer 3 get coffee  
Time 7 customer 2 get coffee  
Time 14 customer 4 get coffee  
Time 15 customer 5 get coffee  
Time 15 customer 6 get coffee  
The customer who waited the longest is : 6
The customer waited for 4 minutes
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
    
class Customer:
    def __init__(self, si, pi):
        self.si = si
        self.pi = pi
        
print(' ***Cafe***')
log = input('input : ').split('/')

cafe = Queue()
b1 = Queue()
b2 = Queue()
time = 0

for cs in log:
    si = int(cs.split(',')[0])
    pi = int(cs.split(',')[1])

    cafe.enqueue(Customer(si, pi))

