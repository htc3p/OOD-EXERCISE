class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def listLength(self):
        curNode = self.head
        length = 0
        while curNode is not None:
            length += 1
            curNode = curNode.next
        return length

    def append(self, newNode):
        # head=>John->None
        if self.head is None:
            self.head = newNode
        else:
            # head=>John->Ben->None || John -> Matthew
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def addHead(self, newNode):
        # data => Matthew, next => None
        tempNode = self.head   # John
        self.head = newNode    # Matthew
        self.head.next = tempNode
        del tempNode

    def insert(self, pos, newNode):
        # head => 10->20->None || newNode => 15->None || pos => 1
        if pos == 0:
            self.addHead(newNode)
            return 
        if pos < 0 or pos > self.listLength():
            print("Invalid position")
            return
        
        curNode = self.head  # 10, 20
        curPos = 0           # 0, 1
        while True:
            if curPos == pos:
                previousNode.next = newNode
                newNode.next = curNode
                break
            previousNode = curNode
            curNode = curNode.next
            curPos += 1

    def deleteHead(self):
        if not self.isEmpty():
            previousNode = self.head
            self.head = self.head.next
            previousNode.next = None
        else:
            print("Linked list is empty. Delete failed")

    def pop(self, pos):
        if pos < 0 or pos > self.listLength():
            print("Invalid position")
            return
        if not self.isEmpty():
            if pos == 0:
                self.deleteHead()
                return
            
            # head => 10->20->15->None || pos=>1
            curNode = self.head
            curPos = 0
            while True:
                if curPos == pos:
                    previousNode.next = curNode.next
                    curNode.next = None
                    break
                previousNode = curNode
                curNode = curNode.next
                curPos += 1
        else:
            print("List is empty") 

    def deleteEnd(self):
        if not self.isEmpty():
            if self.head.next is None:
                self.deleteHead()
                return
            
            # head=>John->Ben->Matthew->None
            lastNode = self.head
            while lastNode.next is not None:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None
        else:
            print("Linked list is empty. Delete failed")
            
    def printList(self):
        # head=>John->Ben->Matthew->None
        if self.head is None:
            print("List is empty")
            return
        curNode = self.head
        while True:
            if curNode is None:
                break
            print(curNode.value)
            curNode = curNode.next


linkedList = LinkedList()
firstNode = Node(10)
linkedList.append(firstNode)
secondNode = Node(20)
linkedList.append(secondNode)
thirdNode = Node(15)
linkedList.append(thirdNode)
linkedList.pop(2)
# linkedList.deleteHead()
linkedList.printList()