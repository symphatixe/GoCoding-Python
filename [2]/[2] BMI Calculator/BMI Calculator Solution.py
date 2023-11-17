# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
float_height = float(height)
float_weight = float(weight)

height_squared = float_height**2
print(int(float_weight // height_squared))