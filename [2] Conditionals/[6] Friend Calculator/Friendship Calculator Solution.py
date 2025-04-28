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

friend_count = 0

friend_count += combined_name.count("l")
friend_count += combined_name.count("o")
friend_count += combined_name.count("v")
friend_count += combined_name.count("e")

total_count = int(str(true_count) + str(friend_count))

if (total_count < 10 or total_count > 90):
    print(f"Your love score is {total_count} and you go together like coke and mentos.")
elif (total_count >= 40 and total_count <= 50):
    print(f"Your score is {total_count} you are alright together.")
else:
    print(f"Your score is {total_count}.")