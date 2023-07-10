print(" *** Rank score ***")
print("Enter ID and Score end with ID : ", end="")
id_score = list(map(str, input().split()))

that_std_id = id_score[-1]
id_score = id_score[:-1]

print(id_score)
print(that_std_id)

id_score_dict = {}
for i in range(0, len(id_score), 2):
    id_score_dict[id_score[i]] = float(id_score[i + 1])

print(id_score_dict)

found = False
for i in range(0, len(id_score), 2):
    if id_score[i] == that_std_id:
        print((i // 2) + 1)
        found = True
        break

if not found:
    print("Not Found")