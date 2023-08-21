'''
Enter Input : 3
__#
_##
###
Enter Input : -3
###
_##
__#
'''

def staircase(n, i):
    if n > 0:
        if i > n:
            pass
        else:
            print(("_"*(n-i)) + "#"*(i))
            return staircase(n,i+1)
    
    elif n < 0:
        if i > -n:
            pass
        else:
            print("_"*(i-1) + "#"*((-n)-(i-1)))
            return staircase(n,i+1)
    else:
        print("Not Draw!")

staircase(int(input("Enter Input : ")), 1)