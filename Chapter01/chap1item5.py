class Canvas:
    def __init__(self, w, h, bg='.'):
        self.w = w
        self.h = h
        self.canvas = [[bg] * w for _ in range(h)]

    def draw(self):
        for row in self.canvas:
            print(''.join(row))

    def draw_rectangle(self, top_left_pos, w, h, brush='*'):
        x1, y1 = top_left_pos
        for y in range(y1, y1 + h):
            for x in range(x1, x1 + w):
                if 0 <= x < self.w and 0 <= y < self.h:
                    self.canvas[y][x] = brush

    def draw_circle(self, pos, r, brush='*'):
        x1, y1 = pos
        for y in range(self.h):
            for x in range(self.w):
                if ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5 <= r:
                    self.canvas[y][x] = brush

    @staticmethod
    def __triangle_area(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    @staticmethod
    def __find_bounding_box(*points):
        min_x, min_y = points[0]
        max_x, max_y = points[0]
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        return (min_x, max_y), (max_x, min_y)

    @staticmethod
    def __point_in_triangle(p, p1, p2, p3):
        a1 = Canvas.__triangle_area(p, p2, p3)
        a2 = Canvas.__triangle_area(p, p1, p2)
        a3 = Canvas.__triangle_area(p, p1, p3)
        a = Canvas.__triangle_area(p1, p2, p3)
        return a == a1 + a2 + a3

    def draw_triangle(self, p1, p2, p3, brush='*'):
        tl, br = self.__find_bounding_box(p1, p2, p3)
        min_x, max_y = tl
        max_x, min_y = br
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if 0 <= x < self.w and 0 <= y < self.h:
                    p = (x, y)
                    if self.__point_in_triangle(p, p1, p2, p3):
                        self.canvas[y][x] = brush


num = int(input('Enter Input : '))
w = (num + 2) * 2

canvas = Canvas(w, w)

canvas.draw_rectangle((w // 2, 0), w // 2, w // 2, brush='+')
canvas.draw_rectangle((w // 2 + 1, 1), num, num, brush='#')

canvas.draw_rectangle((0, w // 2), w // 2, w // 2, brush='#')
canvas.draw_rectangle((1, w // 2 + 1), num, num, brush='+')

canvas.draw_triangle((w // 2 - 1, 0), (w // 2 - 1, w // 2 - 1), (0, w // 2 - 1), brush='#')
canvas.draw_triangle((w // 2, w // 2), (w - 1, w // 2), (w // 2, w - 1), brush='+')

canvas.draw()