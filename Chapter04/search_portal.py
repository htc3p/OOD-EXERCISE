class Queue():
    def __init__(self, list=None):
        if list==None:
            self.items = []
        else:
            self.items = list

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def verify_room(w, h, map):
    found_starting_point = False
    h_valid = (len(map)==h)
    w_valid = True

    for i in map:
        if len(i)!=w:
            w_valid = False

        for j in i:
            if j == 'F':
                found_starting_point = True

    return found_starting_point and w_valid and h_valid

def find_portal(w, h, map, map_2d):
    if not verify_room(w, h, map):
        print('Invalid map input.')
        return

    # find starting position
    for i, j in enumerate(map):
        for n, m in enumerate(j):
            if m == 'F':
                start_x = n
                start_y = i

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # Fix
    path = Queue([(start_x, start_y)])
    found_portal = False

    while not path.isEmpty():
        print('Queue:', path.items)
        x, y = path.dequeue()

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if not (0 <= new_x < w and 0 <= new_y < h):
                continue
            if map_2d[new_y][new_x] == '_':
                path.enqueue((new_x, new_y))
                map_2d[new_y][new_x] = '*'
            if map_2d[new_y][new_x] == 'O':
                print('Found the exit portal.')
                found_portal = True
                break
        if found_portal:
            break
    else:
        print('Cannot reach the exit portal.')
            

width, height, room = input('Enter width, height, and room: ').split()
w, h = int(width), int(height)
map = room.split(',')
map_2d = [[c for c in row] for row in room.split(',')]
# print(map)

find_portal(w, h, map, map_2d)