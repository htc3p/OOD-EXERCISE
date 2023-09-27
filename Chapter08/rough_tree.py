def calculate_node(val, pos):
    if val[pos] != -999:
        return
    
    calculate_node(val, 2*pos+1)   # left
    calculate_node(val, 2*pos+2)   # right

    x = min(val[2*pos+1], val[2*pos+2])
    val[pos] = x
    val[2*pos+1] -= x
    val[2*pos+2] -= x

    return val


n, val = input("Enter Input : ").split('/')
n = int(n)
val = list(map(int, val.split()))

if (n//2)+1 == len(val):
    while len(val) < n:
        val.insert(0, -999)
    
    print(sum(calculate_node(val, 0)))
else:
    print('Incorrect Input') 