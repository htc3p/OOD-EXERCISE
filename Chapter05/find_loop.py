'''
ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง
โดยมีการรับ input ดังนี้
1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list
2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2
ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        if self.size()==1 and self.head.next is None:
            cur, s = self.head, str(self.head.value) + " "
        else:
            cur, s = self.head, str(self.head.value) + "->"

        while cur.next != None:
            if cur.next.next is None:
                s += str(cur.next.value) + " "
            else:
                s += str(cur.next.value) + "->"
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node    # new_node is our new tail node

    def addHead(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node    # new_node is our new head node

    def insert(self, pos, item):
        insertNode = Node(item)
        if pos == 0:
            self.addHead(item)
            return
        if pos > 0:
            if pos >= self.size() - 1:
                self.append(item)
                return
            else:
                node = self.head
                for _ in range(0, pos):
                    node = node.next
                previousNode = node
                nextNode = previousNode.next
                previousNode.next = insertNode
                insertNode.previous = previousNode
                nextNode.previous = insertNode
                insertNode.next = nextNode
        else:
            if pos <= -self.size():
                self.addHead(item)
                return
            else:
                node = self.tail
                for _ in range(-1, pos-1, -1):
                    node = node.previous
                previousNode = node
                nextNode = previousNode.next
                previousNode.next = insertNode
                insertNode.previous = previousNode
                nextNode.previous = insertNode
                insertNode.next = nextNode

    def search(self, item):
        curNode = self.head
        while curNode is not None:
            if curNode.value == item:
                return "Found"
            curNode = curNode.next
        return "Not Found"

    def index(self, item):
        idx = 0
        curNode = self.head
        while curNode is not None:
            if curNode.value == item:
                return idx
            curNode = curNode.next
            idx += 1
        return -1

    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if self.size()-1 < pos or pos < 0:
            return "Out of Range"
        if self.size() == 1:
            self.head = None
            self.tail = None
        elif pos == 0:
            newHead = self.head.next
            newHead.previous = None
            self.head = newHead
        elif pos == self.size()-1:
            newTail = self.tail.previous
            newTail.next = None
            self.tail = newTail
        else:
            node = self.head
            for _ in range(0, pos):
                node = node.next
            previousNode = node.previous
            nextNode = node.next
            if previousNode is not None:
                previousNode.next = nextNode
                nextNode.previous = previousNode
        return "Success"
    
    def cycleDetect(self):
        if self.head == None:
            return False
        fast = self.head
        slow = self.head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
    def _find_node_by_index(self, index):
        if index < 0:
            node = self.tail
            for _ in range(-1, index-1, -1):
                if node is None:
                    break
                node = node.previous
        else:
            node = self.head
            for _ in range(index):
                if node is None:
                    break
                node = node.next
        return node
    
    def set_next(self, idx1, idx2):
        node1 = self._find_node_by_index(idx1)
        node2 = self._find_node_by_index(idx2)  

        if self.isEmpty():
            return "Error! {list is empty}"
        if node1 is None:
            return "Error! {index not in length}: " + str(idx1)
        if node2 is None:
            self.append(idx2)
            return f"index not in length, append : {idx2}"

        node1.next = node2
        return f"Set node.next complete!, index:value = {idx1}:{node1.value} -> {idx2}:{node2.value}"

L = LinkedList()
inp = input('Enter input : ').split(',')

for i in inp:
    if i[0] == 'A':
        data = i[2:]
        L.append(data)
        print(L)
    if i[0] == 'S':
        idx1, idx2 = map(int, i[2:].split(':'))
        result = L.set_next(idx1, idx2)
        print(result)

if L.cycleDetect():
    print("Found Loop")
else:
    print("No Loop")
    print(L)