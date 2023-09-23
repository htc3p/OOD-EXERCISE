'''
ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''

def findMaxIndex(lists):
    index = None
    for i in range(len(lists)):
        if index == None and lists[i] >= 0:
            index = i
        elif index != None and lists[i] > lists[index]:
            index = i
    return index

def selection_sort(l):
    for i in range(len(l)-1, -1, -1):
        if l[i] >= 0:
            max_pos = findMaxIndex(l[:i+1])
            if l[i] < l[max_pos]:
                l[i], l[max_pos] = l[max_pos], l[i]
    return l


num = [int(x) for x in input('Enter Input : ').split()]
print(' '.join(map(str, selection_sort(num))))