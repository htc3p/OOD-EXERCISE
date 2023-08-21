'''
กบเขียวเคโรโระ ต้องการกระโดดจากช่องหมายเลข 0 ไปเลขต่างๆ ไม่เกิน 40 เคโรโระ ต้องการทราบวิธีการไปทั้งหมด 
และจำนวนครั้งที่กระโดดน้อยที่สุด เมื่อเคโรโระสามารถกระโดดได้ทีละ 1 5 7 ช่อง
แต่ว่ากบแดงกิโรโระจะดักโจมตีช่องที่หารด้วย14ลงตัว ทำให้เคโรโระไม่สามารถผ่านช่องเหล่านั้นได้ ถ้าเคโรโระไม่สามารถไปถึงจุดหมายได้ ให้แสดง mission failed

Input number : 3
Minimum Distance is 3
Maximum Way is 1

Input number : 10
Minimum Distance is 2
Maximum Way is 12
'''


def jump(n, passed, distance):
    global way, min_distance, temp_distance
    if n == -1:
        way += 0
    if passed > 0 and passed % 14 == 0:
        jump(-1, 1, 0)
    else:
        if n >= 7:
            jump(n-7, passed+7, distance+1)
        if n >= 5:
            jump(n-5, passed+5, distance+1)
        if n >= 1:
            jump(n-1, passed+1, distance+1)
        if n == 0:
            way += 1
            if distance < min_distance:
                min_distance = distance
        
    
way = 0
min_distance = 99
temp_distance = 0
distance = int(input('Input number : '))   
if distance % 14 == 0:
    print('Mission Failed')
else:
    jump(distance, 0, 0)
    print(f'Minimum Distance is {min_distance}')
    print(f'Maximum Way is {way}')