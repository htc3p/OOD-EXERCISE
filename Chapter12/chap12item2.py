print(" *** Rank score ***")
id_score = list(map(str,input("Enter ID and Score end with ID : ").split()))
that_std_id = id_score[-1]
id_score.pop()
id_score_dict = {}
for id in range(0,len(id_score),2):
    id_score_dict[id_score[id]] = float(id_score[id+1])
print(id_score)
print(that_std_id)
print(id_score_dict)
id_score_dict2 = dict(sorted(id_score_dict.items())) #เรียง key
id_score_dict2 = dict(reversed(list(id_score_dict2.items())))
id_score_dict2 = dict(sorted(id_score_dict2.items(), key=lambda item: item[1])) #เรียง value

ans = list(set(id_score_dict2.values()))
for id in id_score_dict:
    if (that_std_id == id ):
        ans = len(ans) - ans.index(id_score_dict[id])
        break
if (type(ans) == list):
    ans = "Not Found"
print(ans)