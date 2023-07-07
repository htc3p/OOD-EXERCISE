print(" *** BMI ***")
print("Enter your weight(kg) and height(m) : ", end="")
weight, height = map(float, input().split())
bmi = weight / (height*height)
print("Your status is : ", end="")

if bmi<18.5:
    print("Below normal weight.")
elif 18.5 <= bmi < 25:
    print("Normal weight.")
elif 25 <= bmi < 30:
    print("Overweight.")
elif 30 <= bmi < 35:
    print("Case I Obesity.")
elif 35 <= bmi < 40:
    print("Case II Obesity.")
elif bmi >= 40:
    print("Case III Obesity.")