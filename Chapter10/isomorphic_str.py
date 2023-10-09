def isomorphic(string1, string2):
    if(len(string1) != len(string2)):
        return False
    x = [string1.count(char1) for char1 in string1]
    y = [string2.count(char1) for char1 in string2]

    return x == y


string_input = input("Enter str1,str2: ").split(',')
string1 = string_input[0].strip()
string2 = string_input[1].strip()

if isomorphic(string1, string2):
    print(f"{string1} and {string2} are Isomorphic")
else:
    print(f"{string1} and {string2} are not Isomorphic")