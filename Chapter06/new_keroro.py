def jump(target, passed, distance):
    global way, min_distance
    if target < 0:
        way += 0
    if passed > 0 and passed % 14 == 0:
        jump(-1, 1, 0)
    else:
        if target >= 7:
            jump(target-7, passed+7, distance+1)
        if target >= 5:
            jump(target-5, passed+5, distance+1)
        if target >= 1:
            jump(target-1, passed+1, distance+1)
        if target == 0:
            way += 1
            if distance < min_distance:
                min_distance = distance


way = 0
min_distance = 40
target = int(input('Input number : '))
if target%14 == 0:
    print('Mission Failed')
else:
    jump(target, 0, 0)
    print(f'Minimum Distance is {min_distance}')
    print(f'Maximum Way is {way}')