def bon(w):
    eng = 'abcdefghijklmnopqrstuvwxyz'
    sum = 0
    elements = {}
    for char in w:
        if elements.get(char,None) != None:
            elements[char]+=1
        else:
            elements[char] = 1

    for k, v in elements.items():
        if v>1:
            for i, j in enumerate(eng):
                if k==j:
                    sum += (i+1)*4
        
    return sum

secretCode = input("Enter secret code : ")
print(bon(secretCode))