# Starter Code
entry = input("Enter some text\n")
list = []


# Write your code below!
for num in range(len(entry)):
    list.append(entry[num])
    
print("User Input: " + entry)
print("Separated List: " + str(list))