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


class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        
        def __str__(self):
            return str(self.data)
    
    def __init__(self):
        self.root = None
    
    def insert(self, root, data):
        if not root:
            self.root = BST.Node(data)
            return self.root
        else:
            if root.data == data:
                return root
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root
    
    def min_data(self, root):
        if not root:
            return
        if not root.left:
            return root.data
        return self.min_data(root.left)
    
    def max_data(self, root):
        if not root:
            return
        if not root.right:
            return root.data
        return self.max_data(root.right)
    
    def preorder(self, root):
        if root:
            print(root, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root, end=' ')
            self.inorder(root.right)
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root, end=' ')
    
    def breadth(self, root):
        q = Queue()
        q.enQueue(root)
        while q.isEmpty() is not True :
            n = q.deQueue()
            print(n.data, end = ' ')
            if n.left is not None:
                q.enQueue(n.left)
            if n.right is not None:
                q.enQueue(n.right)
    
    def print_tree(self, root, level= 0):
        if root != None:
            self.print_tree(root.right, level + 1)
            print('     ' * level, root)
            self.print_tree(root.left, level + 1)

if __name__ == '__main__':
    T = BST()
    root = None
    root = T.insert(root, 50)
    root = T.insert(root, 60)
    root = T.insert(root, 70)
    root = T.insert(root, 80)
    root = T.insert(root, 55)
    T.print_tree(root)
    T.breadth(root)