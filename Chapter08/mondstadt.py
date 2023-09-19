'''
Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
                พลัง    :   5  4  4  3  2  2  2
                ลำดับ  :   0  1  2  3  4  5  6
จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
    -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
    -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
    -  กลุ่มของอัศวินกลุ่มที่ i จะมีสมาชิกคือ อัศวินลำดับที่ i และลูกน้องของอัศวินลำดับที่ i (รวมลูกน้องของลูกน้องของอัศวินด้วย)
    -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
            -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
            -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน
'''

class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = 0
        
        def __str__(self):
            return str(self.data)
    
    def __init__(self, root = None):
        self.root = None if root is None else root
    
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        else:
            if root.left is None:
                root.left = self._insert(root.left, data)
            elif root.right is None:
                root.right = self._insert(root.right, data)
            else:
                if root.left.left is None or root.left.right is None:
                    root.left = self._insert(root.left, data)
                else:
                    root.right = self._insert(root.right, data)
            return root
        

def getPower(node):
    if node:
        return node.data + getPower(node.left) + getPower(node.right)
    return 0

def findNode(node, a, i=0, d=[]):
    if node:
        if node.left:
            d.append(node.left)
        if node.right:
            d.append(node.right)
        if a == i:
            return node
        return findNode(d.pop(0), a, i+1, d)

def compare(root,i,j):
    cI = getPower(findNode(root,i, 0, []))
    cJ = getPower(findNode(root,j, 0, []))
    if cI < cJ:
        print(f'{str(i)}<{str(j)}')
    elif cI > cJ:
        print(f'{str(i)}>{str(j)}')
    else:
        print(f'{str(i)}={str(j)}')


avl = AVLTree()
n, comp = input("Enter Input : ").split('/')
n = list(map(int, n.split()))
comp = comp.split(',')

for i in n:
    avl.insert(i)

print(sum(n))
for c in comp:
    i, j = c.split()
    compare(avl.root, int(i), int(j))