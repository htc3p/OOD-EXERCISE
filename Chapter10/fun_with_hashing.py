class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, size, max_collision):
        self.size = size
        self.max_collision = max_collision
        self.table = [None] * size

    def __str__(self):
        s = str()
        for i,val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "---------------------------"

    def full(self):
        if not None in self.table:
            print("This table is full !!!!!!")
            exit()

    def insert(self, key, val):
        self.full()
        coll = 0
        bIdx = idx = sum(ord(i) for i in key) % self.size
        while self.table[idx]:
            coll+=1
            print(f"collision number {coll} at {idx}")
            if coll == self.max_collision:
                print("Max of collisionChain")
                break
            idx = (bIdx+(coll**2)) % self.size
        if not self.table[idx]:
            self.table[idx] = Data(key,val)


print(' ***** Fun with hashing *****')
table, data = input('Enter Input : ').split('/')
size, max_collision = map(int, table.split())
h = hash(size, max_collision)
for i in data.split(','):
    key, value = i.split()
    h.insert(key, value) or print(h)