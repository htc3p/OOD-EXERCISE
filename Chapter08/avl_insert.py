'''
ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert และปรับ Balance เรียบร้อยแล้ว
** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
'''

class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
        
        def __str__(self):
            return str(self.data)
        
        def setHeight(self):
            l = self.getHeight(self.left)
            r = self.getHeight(self.right)
            self.height = max(l ,r) + 1
            return self.height
            
        def getHeight(self, node):
            return -1 if node is None else node.height
            
        def getBalanceValue(self):
            return self.getHeight(self.left) - self.getHeight(self.right)
    
    def __init__(self, root = None):
        self.root = None if root is None else root
    
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return self.AVLNode(data)
        else:
            if int(data) < int(root.data):
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
            root = self.rebalance(root)                
            return root
    
    def rebalance(self, node):
        if node is None:
            return node
        balance = node.getBalanceValue()
        if balance == -2:
            if node.right.getBalanceValue() == 1:
                node.right = self.leftRotate(node.right)
            node = self.rightRotate(node)
        elif balance == 2:
            if node.left.getBalanceValue() == -1:
                node.left = self.rightRotate(node.left)
            node = self.leftRotate(node)

        node.setHeight()
        return node

    def leftRotate(self, x) :
        y = x.left
        x.left = y.right
        y.right = x
        x = y
        x.right.setHeight()
        x.setHeight()
        return x
    
    def rightRotate(self, x) :
        y = x.right
        x.right = y.left
        y.left = x
        x = y
        x.left.setHeight()
        x.setHeight()
        return x
    
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


avl = AVLTree()
inp = [e for e in input('Enter Input : ').split()]
for i in inp:
    print(f'Insert : ( {i} )')
    avl.insert(i)
    avl.printTree(avl.root)
    print('--------------------------------------------------')