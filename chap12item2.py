print(" *** Rank score ***")
print("Enter ID and Score end with ID : ", end="")
lst = list(map(str, input().split()))
last_id = lst[len(lst)-1]
lst.pop(len(lst)-1)
print(lst)
print(last_id)

def Convert(list):
    res_dict = {list[i]: float(list[i+1]) for i in range(0, len(lst), 2)}
    return res_dict

dct = Convert(lst)
sortedDict = dict(sorted(dct.items()))
print(sortedDict)

if last_id in sortedDict:
    order = 1
    for key in sortedDict:
        if key == last_id:
            break
        order += 1
    print(order)
else:
    print("Not Found")