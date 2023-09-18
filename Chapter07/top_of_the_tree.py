class BST:
    class Node:
        def __init__(self, data, left=None, right=None) -> None:
            self.data = data
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.root = None

    def insert(self, parent_data, child_data):
        self.root = self._insert(self.root, parent_data, child_data)

    def _insert(self, node, parent_data, child_data):
        if node:
            if node.data == parent_data:
                if node.left is None:
                    node.left = BST.Node(child_data)
                else:
                    node.right = BST.Node(child_data)
            node.left = self._insert(node.left, parent_data, child_data)
            node.right = self._insert(node.right, parent_data, child_data)
        
        return node
    
    def print_left(self):
        BST._print_left(self.root.left)
    
    def _print_left(node):
        if node:
            BST._print_left(node.left)
            print(node, end = ' ')

    def print_right(self):
        BST._print_right(self.root.right)

    def _print_right(node):
        if node:
            print(node, end = ' ')
            BST._print_right(node.right)

    def print_tree(self):
        self.print_left()
        print(self.root, end = ' ')
        self.print_right()


T = BST()
inp = input('Enter Input : ').split(',')
T.root = T.Node(inp[0].split()[0])
for i in inp:
    parent_data, child_data = i.split()
    T.insert(parent_data, child_data)

print('Top view : ', end = '')
T.print_tree()