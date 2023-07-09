def odd_even(type, data, mode):
    if type=='S':
        str_output = ''
        for count, char in enumerate(data):
            if mode=="Odd":
                if (count+1)%2 != 0:
                    str_output += char
            elif mode=="Even":
                if (count+1)%2 == 0:
                    str_output += char
        return str_output
    elif type=='L':
        list_temp = data.split(' ')
        list_output = []
        for count, char in enumerate(list_temp):
            if mode=="Odd":
                if (count+1)%2 != 0:
                    list_output.append(char)
            elif mode=="Even":
                if (count+1)%2 == 0:
                    list_output.append(char)
        return list_output
                

print("*** Odd Even ***")
type, data, mode = input("Enter Input : ").split(',')
print(odd_even(type, data, mode))