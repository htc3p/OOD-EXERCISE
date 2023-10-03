'''
พี่โบ๊ทได้ไปเล่นเกมนึง ที่ชื่อว่า Honkai: Star Rail ซึ่งเป็นเกมแนว Turn-Based แล้วพี่โบ๊ทได้ไปสนใจระบบ Combat นึงที่ใช้ค่า Speed (SPD) ของตัวละครซึ่งเป็นค่าบ่งบอกว่า ใครจะได้เทิร์นก่อน โดยวัดจากค่า Action 
ซึ่งวิธีการคำนวณโดยการ เอา 10000 หารด้วย Speed จะได้เป็นค่า Action แล้วตอน Turn แรกใครมีค่า Action น้อยที่สุดจะได้เป็นคนเริ่มก่อน

เช่น
Boat มีค่า SPD 100 / Pune มีค่า SPD 115 / Yaya มีค่า SPD 120

ในก่อน Turn แรก
Boat จะมีค่า Action 10000 / 100 = 100
Pune จะมีค่า Action 10000 / 115 = 86 (หารแบบ int คือไม่เอาเศษ)
Yaya จะมีค่า Action 10000 / 120 = 83 (หารแบบ int คือไม่เอาเศษ)

Turn 1 Yaya จะได้เป็นคนเริ่มก่อนก็จะเป็น
0-Yaya
3-Pune
17-Boat

เมื่อจบ Action ก็ให้ค่า Action เท่ากับ 10000 / SPD เช่นเดิม
จากนั้น Turn ต่อไป Pune จะเป็นคนเริ่มเล่นต่อไปโดยทุกๆ คนจะหักลบค่า Action ของคนที่ได้เทิร์นถัดไป

Turn 2 ก็จะเป็น
0-Pune
14-Boat
80-Yaya

ไปเรื่อยๆ
ข้อมูลนำเข้า : <ค่า SPD> <ชื่อตัวละคร>/<จำนวนเทิร์น>
ข้อมูลนำออก : แสดงค่า Action และชื่อตัวละคร ตามลำดับที่ได้เทิร์น

หมายเหตุ: ห้ามใช้ฟังก์ชัน built-in สำเร็จรูปในการ sort เช่น .sort() sorted()
'''

def hiddensort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j][2] <= list[j-1][2]:
            if list[j][2] == list[j-1][2]:
                if list[j][0] > list[j-1][0]:
                    list[j], list[j-1] = list[j-1], list[j]
                    j-=1
                else:
                    break
            elif list[j][2] < list[j-1][2]:
                list[j], list[j-1] = list[j-1], list[j]
                j-=1
            else:
                break
    return list

characters, turns = input('Enter list of character: ').split('/')
characters = characters.split(',')
characters_stats = []
for c in characters:
    temp = []
    speed, character_name = c.split(' ')
    temp.append(int(speed))
    temp.append(character_name)
    temp.append(int(10000/temp[0]))
    characters_stats.append(temp)

result = hiddensort(characters_stats)
print('------------------------------')
for i in range(0, int(turns)):
    print(f'Turn {i+1}')
    index = i
    if index >= len(result):
        index -= len(result)
    next_action = result[0][2]
    for j in range(0, len(result)):
        result[j][2] -= next_action
        print(f'{result[j][2]}-{result[j][1]}')
    temp = result.pop(0)
    temp[2] = int(10000/temp[0])
    result.append(temp)
    result = hiddensort(result)
    print('------------------------------')