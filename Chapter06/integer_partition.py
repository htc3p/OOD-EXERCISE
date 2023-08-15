# Integer Partition
def partitions(n, s, d=None, display=[]):
    global lines
    if d is None:
        d = n
    if n == 0:
        if display == []:
            print(n)
        elif lines < s:
            print(' + '.join(display))
            lines += 1
        elif lines == s:
            print('. . .')
            lines += 1
        return 1
    if n < 0 or d == 0:
        return 0
    
    return partitions(n-d, s, d, display + [str(d)]) + partitions(n, s, d-1, display)

if __name__ == '__main__':
    lines = 0
    n, s = map(int, input('Enter n, s: ').split())
    ways = partitions(n, s)
    print(f'Total: {ways}')