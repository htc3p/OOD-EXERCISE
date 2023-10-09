'''
หาทางที่สั้นที่สุดจากการเดินไปในแต่ละจุด
โดยแต่ละบรรทัดแสดงการเดินในแต่ละครั้ง โดยจะเลือกเส้นทางที่สั้นที่สุดเสมอ พร้อมบอกระยะทางเป็นทศนิยม 4 ตำแหน่ง และจะสิ้นสุดการเดิน เมื่อเดินไปครบทุกจุด

โดย Input จะมี 2 ส่วนคือ

    1. List of Points in 2D เช่น 1 1,2 2,3 3 แทนจุดแต่ละจุดที่สามารถเดินไปได้ (x1 y1,x2 y2,x3 y3)
    2. Starting Point คือจุดที่จะเริ่มเดิน
'''


def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def find_path(points, start, path=[]):
    if len(points) == 0:
        return
    if start in points:
        points.remove(start)
        min_distance = float('inf')
        next_point = None
        for point in points:
            if distance(start, point) < min_distance:
                min_distance = distance(start, point)
                next_point = point
        if next_point is not None:
            print(f'{start} -> {next_point} | The distance is {min_distance:.4f}')
            find_path(points, next_point, path)
    else:
        print(f'{start} is not in {points}')
        return
        
points, start = input('Enter a list of points: ').split('/')
points = list(map(lambda x: list(map(float, x.split())), points.split(',')))
start = list(map(float, start.split()))
find_path(points, start, path=[start])