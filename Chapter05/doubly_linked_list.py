'''
โดยรูปแบบ Input มีดังนี้
1. append    ->  AP
2. addHead  ->  AH
3. search      ->  SE
4. index        ->   ID
5. size          ->   SI
6. pop          ->   PO
7. insert       ->   IS
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
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
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


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())