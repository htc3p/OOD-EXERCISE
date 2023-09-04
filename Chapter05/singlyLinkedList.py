class Node:
    def __init__(self, val):
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

    def addHead(self, val):
        new = Node(val)
        if self.isEmpty():
            self.head = new
        else:
            cur = self.head
            self.head = new
            self.head.next = cur
            del cur

    def insert(self, val, pos):
        if pos < 0 or pos > self.listLength():
            return 'Invalid Position'
        elif pos == 0:
            self.addHead(val)
        elif pos == self.listLength():
            self.addTail(val)
        else:
            new = Node(val)
            cur = self.head
            for _ in range(pos-1):
                cur = cur.next
            new.next = cur.next
            cur.next = new
            del cur

    def removeHead(self):
        if self.isEmpty():
            return 'Empty'
        else:
            cur = self.head
            self.head = cur.next
            del cur

    def removeTail(self):
        if self.isEmpty():
            return 'Empty'
        else:
            cur = self.head     # 3 4 1 2
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None
            del cur

    def remove(self, pos):
        if pos < 0 or pos > self.listLength():
            return 'Invalid Position'
        elif pos == 0:
            self.removeHead()
        elif pos == self.listLength():
            self.removeTail()
        else:
            cur = self.head
            for _ in range(pos-1):
                cur = cur.next
            cur.next = cur.next.next
            del cur

    def search(self, val):
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return True
            cur = cur.next
        return False
    
    def reverse(self): #6->1->3
        prev, cur = None, self.head 
        while cur is not None:
            temp = cur.next     
            cur.next = prev     
            prev = cur         
            cur = temp          
        self.head = prev


if __name__ == '__main__':
    ll = LinkedList()
    ll.addTail(1)
    ll.addTail(2)
    ll.addTail(3)
    ll.addTail(4)
    ll.addHead(5)
    ll.insert(6, 1)
    print(ll)
    ll.removeHead()
    print(ll)
    ll.removeTail()
    print(ll)
    ll.remove(2)
    print(ll)
    print(ll.search(3))
    print(ll.search(11))
    ll.reverse()
    print(ll)
    # print(ll.listLength())