'''
ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''

def bubble_sort(l):
    for i in range(len(l)-1, 0,-1):
        swaped = False
        for j in range(i):
            if compare(l[j], l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
                swaped = True
        if not swaped:
            break
    return l

def compare(s1, s2):
    char1 = next((i for i in s1 if i.isalpha()), None)
    char2 = next((i for i in s2 if i.isalpha()), None)

    if char1 < char2:
        return False
    else:
        return True

string = input('Enter Input : ').split()
print(' '.join(bubble_sort(string)))