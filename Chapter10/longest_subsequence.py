'''
แสดงค่าจำนวนตัวเลขมากที่สุด ที่สามารถเรียงจากน้อยไปมากได้โดยไม่สลับตำแหน่ง
'''
class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        
    def __str__(self):
        return str(self.items)
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)
    

def LIS(nums):
    result = Stack()
    result_list = []

    for i, num in enumerate(nums):
        if result.isEmpty() or num > result.peek():
            result.push(num)
        else:
            while not result.isEmpty() and num <= result.peek():
                result.pop()
            result.push(num)
        result_list.append(list(result.items))
        print(f'{i+1} : {result}')
    return max(map(len, result_list))

    
data = list(map(int, input('Data : ').split()))
max_lis= LIS(data)
print(f'longest increasing subsequence : {max_lis}')