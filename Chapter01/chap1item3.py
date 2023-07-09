print(" *** Summation of each digit ***")
num = int(input("Enter a positive number : "))

total = 0
if len(str(num)) <= 30:
    for i in str(num):
        total += int(i)

print("Summation of each digit = ", total)