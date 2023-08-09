def getFact(n):
    if n>=1:
        return n*getFact(n-1)
    else:
        return 1
    
num = int(input('Enter Number : '))
print(f'{num}! = {getFact(num)}')