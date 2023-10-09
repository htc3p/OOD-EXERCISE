'''
หาค่าที่น้อยที่สุดใน Table จากนั้นค่าค่าที่มากที่สุดใน Rows นั้นและหาค่าที่มากที่สุด Column นั้นตามลำดับ โดย Input จะประกอบไปด้วยขนาดกว้างยาวของ Table , ข้อมูลในแต่ละ Cell 
'''

def find_col_index(table, value):
    for i, row in enumerate(table):
        for j, col in enumerate(row):
            if col == value:
                return j


size, data = input('input : ').split(',')
size = list(map(int, size.split()))
data = list(map(int, data.split()))

table = []
for i in range(size[0]):
    row = []
    for j in range(size[1]):
        row.append(data[i*size[1] + j])
    table.append(row)


min_value = float('inf')
max_in_min_row = float('-inf')
max_in_min_col = float('-inf')

for row in table:
    for col in row:
        if col <= min_value:
            min_value = col

for row in table:
    if min_value in row:
        for col in row:
            if col > max_in_min_row:
                max_in_min_row = col

index = find_col_index(table, max_in_min_row)
for row in table:
    if row[index] > max_in_min_col:
        max_in_min_col = row[index]

print(max_in_min_col)