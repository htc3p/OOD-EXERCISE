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
        def __init__(self, data: float) -> None:
            self.data = data
            self.left = None
            self.right = None
        
        def __str__(self) -> str:
            return str(self.data)
    
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, root: Node, data: float) -> Node:
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
    
    def min_data(self, root: Node) -> float:
        if not root:
            return
        if not root.left:
            return root.data
        return self.min_data(root.left)
    
    def max_data(self, root: Node) -> float:
        if not root:
            return
        if not root.right:
            return root.data
        return self.max_data(root.right)
    
    def preorder(self, root: Node) -> None:
        if root:
            print(root, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root: Node) -> None:
        if root:
            self.inorder(root.left)
            print(root, end=' ')
            self.inorder(root.right)
    
    def postorder(self, root: Node) -> None:
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root, end=' ')
    
    def breadth(self, root: Node) -> None:
        q = Queue()
        if root:
            print(root, end=' ')
            if root.left:
                q.enQueue(root.left)
            if root.right:
                q.enQueue(root.right)
            if not q.isEmpty():
                self.breadth(q.deQueue())
    
    def print_tree(self, root: Node, level: int = 0) -> None:
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
    T.print_tree(root)