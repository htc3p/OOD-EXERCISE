def jump(inp, start=[]):
    list = []
    if start != [] and sum(start) % 14 == 0 or sum(start) > inp:
        return []
    if sum(start) == inp:
        return [start]
    
    list += jump(inp, start + [7])
    list += jump(inp, start + [5])
    list += jump(inp, start + [1])
    return list

target = int(input('Input number : '))

if target%14 == 0:
    print('Mission Failed')
else:
    n = jump(target)
    # print(n)
    print(f'Minimum Distance is {len(min(n, key=len))}')
    print(f'Maximum Way is {len(n)}')