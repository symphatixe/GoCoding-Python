# Starter Code
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n") 
name2 = input("What is their name? \n")


# Write your code below!
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

if (total < 10 and total > 90):
    print(f"Your love score is {total} and you go together like coke and mentos.")
elif (total >= 40 and total <= 50):
    print(f"Your score is {total} you are alright together.")
else:
    print(f"Your score is {total}.")