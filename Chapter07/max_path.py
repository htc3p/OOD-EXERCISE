def find_max_path(tree, temp=[], index=0):
    global max_path
    if tree == [-1]:
        max_path = [-1]
        return
    if index >= len(tree):
        max_path = temp.copy() if sum(temp) > sum(max_path) else max_path
        return
    temp.append(tree[index])
    find_max_path(tree, temp, 2*index+1)
    if 2*index+2 < len(tree):
        find_max_path(tree, temp, 2*index+2)
    temp.pop()
        

inp = [int(i) for i in input('Enter tree: ').split()]
max_path = [-999999999999]
find_max_path(inp)
print(f'Maximum path: {max_path}')