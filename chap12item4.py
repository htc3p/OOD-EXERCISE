def rotate(str, n):
    return str[n:] + str[:n]

def check_rotation(str1, str2):
    temp1 = str1
    temp2 = str2

    rounds = 0
    while True:
        temp1 = rotate(temp1, -1)
        temp2 = rotate(temp2, 1)
        rounds += 1

        if rounds<=5:
            print(rounds, temp1, temp2)

        if (temp1==str1) and (temp2==str2):
            break
    return rounds

print("*** String Rotation ***")
str1, str2 = input("Enter 2 strings : ").split()

rounds = check_rotation(str1, str2)
if rounds==6:
    print(rounds, str1, str2)
elif rounds>6:
    print(" . . . . . ")
    print(rounds, str1, str2)
print("Total of ", rounds, "rounds.")