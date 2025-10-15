# Starter Code
print("Welcome to the Friendship Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


# Write your code below!


combined_name = name1.lower() + name2.lower()

friend_count = 0

friend_count += combined_name.count("f")
friend_count += combined_name.count("r")
friend_count += combined_name.count("i")
friend_count += combined_name.count("e")
friend_count += combined_name.count("n")
friend_count += combined_name.count("d")

ship_count = 0

ship_count += combined_name.count("s")
ship_count += combined_name.count("h")
ship_count += combined_name.count("i")
ship_count += combined_name.count("p")

score = int(str(friend_count) + str(ship_count))

if (score < 10 or score > 90):
    print(f"Your friendship score is {score} and you are super friends!")
elif (score >= 40 and score <= 50):
    print(f"Your friendship score is {score} you are alright friends.")
else:
    print(f"Your friendship score is {score}.")