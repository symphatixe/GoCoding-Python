# Starter Code
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))


# Write your code below!
height_squared = height**2
bmi = round(weight / height_squared)

if (bmi < 18.5):
    print(f"Your BMI is {bmi}, you are underweight.")
elif (bmi < 25):
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif (bmi < 30):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif (bmi < 35):
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
