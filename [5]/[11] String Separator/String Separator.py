# Starter Code
entry = input("Enter some text\n")
list = []
list2 = []


# Write your code below!
# Ilia

for i in entry:
    list.append(i)
    list2.append(i)

for i in range(len(list)):
    if (list[i] == "v"):
        print(i)
        list[i] = "p"
    
for i in list2:
    if (i == "v"):
        print(i)
        i = "p"
    
print(list)
print(list2)