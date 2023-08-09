'''
รับ input มา1ชุดให้เก็บเป็น LinkedList และจำนวน k โดยคั่นด้วย /
output ให้แสดง index ปัจจุบันที่หารด้วย k ลงตัว value ปัจจุบัน next value ไม่มีเป็น -1
แต่ถ้า k มีค่ามากว่า size ของ LinkedList แสดง Over length
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(item)

    def search(self, pos):
        cur = self.head
        curPos = 0
        while cur is not None:
            if curPos == pos:
                return cur.value
            cur = cur.next
            curPos += 1
        return -1

    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

def index_divide_by_k(L:LinkedList, k:int):
    if k > L.size():
        print('Over length')
        return
    for i in range(L.size()):
        if i%k==0:
            print(f'Now index {i} value is {L.search(i)} next value is {L.search(i+1)}')
    
lst, k = input('Input : ').split('/')
L = LinkedList()
for i in lst.split(' '):
    L.append(i)

index_divide_by_k(L, int(k))