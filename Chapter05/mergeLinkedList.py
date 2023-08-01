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
    

L1 = LinkedList()
L2 = LinkedList()
inp = input('Enter Input (L1,L2) : ').split(' ')

list1 = [e for e in inp[0].split('->')]
list2 = [e for e in inp[1].split('->')]

for i in list1:
    L1.append(i)
for j in list2:
    L2.append(j)

print("L1    :", L1)
print("L2    :", L2)
print("Merge : ", L1, L2.reverse(), sep='')