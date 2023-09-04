class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        
        cur = self.head
        out = ''
        while cur is not None:
            out += str(cur.val) + ' '
            cur = cur.next
        
        return out

    def isEmpty(self):
        return self.head == None
    
    def listLength(self):
        cur = self.head
        len = 0
        while cur is not None:
            len += 1
            cur = cur.next
        return len
    
    def addTail(self, val):
        new = Node(val)
        if self.isEmpty():
            self.head = new
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new
    
    def reverse(self): 
        prev, cur = None, self.head
        while cur is not None:
            temp = cur.next     
            cur.next = prev     
            prev = cur         
            cur = temp          
        self.head = prev

    def mergeTwoLists(self, list2):
        temp = Node()
        cur = temp

        l1 = self.head
        l2 = list2.head

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        self.head = temp.next
    

L1 = LinkedList()
L2 = LinkedList()
inp = input('Enter Input (L1,L2) : ').split(' ')

list1 = [e for e in inp[0].split('->')]
list2 = [e for e in inp[1].split('->')]

for i in list1:
    L1.addTail(i)
for j in list2:
    L2.addTail(j)

print("L1    :", L1)
print("L2    :", L2)
L2.reverse()
L1.mergeTwoLists(L2)
print("Merge :", L1)
# print(L1.reverse())