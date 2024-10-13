# Starter Code
entry = input("Enter some text\n")
list1 = []


# Write your code below!
for num in range(len(entry)):
    list1.append(entry[num])

print("User Input: " + entry)
print(f"Separated List: {list1}")