# ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = 0
        
    def __str__(self):
        s = ''
        for ele in self.items:
            s += str(ele)+' '
        return s
    
    def push(self, data):
        self.items.append(data)
        self.size += 1
    
    def pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items)==0

class BST:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
        
        def __str__(self):
            return str(self.data)
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BST._insert(self.root, data)
        return self.root

    def _insert(root, data):
        if root is None:
            return BST.Node(data)
        else:
            if data < root.data:
                root.left = BST._insert(root.left, data)
            else:
                root.right = BST._insert(root.right, data)
        return root
    
    def inorder(self, node):
        if node is None:
            return
        
        if node.data in ['+', '-', '*', '/']:
            print('(', end='')
        self.inorder(node.left)
        print(node.data, end='')
        self.inorder(node.right)
        if node.data in ['+', '-', '*', '/']:
            print(')', end='')
    
    def preorder(self, node):
        if node is None:
            return
        
        print(node.data, end='')
        self.preorder(node.left)
        self.preorder(node.right)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
S = Stack()
inp = [i for i in input('Enter Postfix : ')]
for i in inp:
    if i in '+-*/':
        r = S.pop()
        l = S.pop()
        S.push(T.Node(i,l,r))
    else :
        S.push(T.Node(i))

root = S.pop()
print('Tree :')
T.printTree(root)
print('--------------------------------------------------')
print('Infix :', end=' ')
T.inorder(root)
print()
print('Prefix :', end=' ')
T.preorder(root)
print()