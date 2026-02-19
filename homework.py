working = float(input("Enter yourt height in cm:"))
absent = float(input("enter your weight in kg:"))

BMI = absent * (working/100)**2

print("your BMI is", BMI)

if BMI > 75:
    print("you will not be able to sit in the chair for exam")
elif BMI == 75:
    print("you will  be able to sit for the exam")
else:
    print("nice, you can sit for your exam ")
    print("exam time !!! The End")