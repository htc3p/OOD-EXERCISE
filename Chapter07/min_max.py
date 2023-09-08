class Queue:
    def __init__(self, q = None):
        if q == None:
            self.item = []
        else:
            self.item = q

    def enQueue(self, i):
        self.item.append(i)

    def deQueue(self):
        return self.item.pop(0)
    
    def isEmpty(self):
        return self.item == []
    
    def size(self):
        return len(self.item)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BST._insert(self.root, data)
        return self.root

    def _insert(root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._insert(root.left, data)
            else:
                root.right = BST._insert(root.right, data)
        return root
    
    def findMin(self):
        return BST._findMin(self.root)
    
    def _findMin(root):
        if root is None:
            return None
        else:
            while root.left is not None:
                root = root.left
        return root
    
    def findMax(self):
        return BST._findMax(self.root)
    
    def _findMax(root):
        if root is None:
            return None
        else:
            while root.right is not None:
                root = root.right
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

T.printTree(root)
print('--------------------------------------------------')
print(f'Min : {T.findMin()}')
print(f'Max : {T.findMax()}')