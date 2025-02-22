# Starter Code
entry = input("Enter some text\n")
list1 = []


# Write your code below!
for position in range(len(entry)):
    list1.append(entry[position])

for letter in entry:
    list1.append(letter)

print("User Input: " + entry)
print(f"Separated List: {list1}")