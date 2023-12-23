# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n") 
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1.lower() + name2.lower()

true_count = 0

true_count += combined_name.count("t")
true_count += combined_name.count("r")
true_count += combined_name.count("u")
true_count += combined_name.count("e")

love_count = 0

love_count += combined_name.count("l")
love_count += combined_name.count("o")
love_count += combined_name.count("v")
love_count += combined_name.count("e")

true = str(true_count)
love = str(love_count)
total = true + love
int_total = int(total)

if (int_total < 10 and int_total > 90):
    print("Your love score is " + str(int_total) + " and you go together like coke and mentos.")
elif (int_total >= 40 and int_total <= 50):
    print("Your score is " + str(int_total) + " you are alright together.")
else:
    print("Your score is " + str(int_total) + ".")