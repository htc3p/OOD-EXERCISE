class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.parent = None  # Add a parent pointer

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left:
            new_root.left.parent = node  # Update the parent pointer
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node is node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root

        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right:
            new_root.right.parent = node  # Update the parent pointer
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node is node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.right = node
        node.parent = new_root

        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rebalance(self, node):
        if node is None:
            return None

        # Update height
        self._update_height(node)

        # Get the balance factor
        balance = self._balance(node)

        # Left heavy
        if balance > 1:
            if self._balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right heavy
        if balance < -1:
            if self._balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            new_node = TreeNode(key)
            if self.root is None:
                self.root = new_node
            return new_node

        if key < node.key:
            node.left = self._insert(node.left, key)
            node.left.parent = node  # Update the parent pointer
        else:
            node.right = self._insert(node.right, key)
            node.right.parent = node  # Update the parent pointer

        return self._rebalance(node)

    def get_node(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.get_node(node.left, key)
        return self.get_node(node.right, key)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level, node.key)
            self.print_tree(node.left, level + 1)
    
    def breadth_first_search(self, node):

        if node is None:
            return
        dict_node = {}
        queue = []
        queue.append([node, node.key, 0]) # node, key, level
        node.key = 666

        while len(queue) > 0:
            cur_node, cur_key, level = queue.pop(0)
            if level not in dict_node:
                dict_node[level] = [cur_key]
            else:
                dict_node[level].append(cur_key)
            if cur_node.left and cur_node.left.key != 666:
                queue.append([cur_node.left, cur_node.left.key, level+1])
                cur_node.left.key = 666
            if cur_node.right and cur_node.right.key != 666:
                queue.append([cur_node.right, cur_node.right.key, level+1])
                cur_node.right.key = 666
            if cur_node.parent and cur_node.parent.key != 666:
                queue.append([cur_node.parent, cur_node.parent.key, level+1])
                cur_node.parent.key = 666
        
        for i in range(len(dict_node)):
            for j in dict_node[i]:
                print(j, end=' ')
            print()


avl_tree = AVLTree()
inp, target = input('Enter node and burn node : ').split('/')
elements = inp.split()

for i in elements:
    avl_tree.insert(int(i))

target_node = avl_tree.get_node(avl_tree.root, int(target))

if target_node is None:
    print(f'There is no {target} in the tree.')
else:
    avl_tree.breadth_first_search(target_node)