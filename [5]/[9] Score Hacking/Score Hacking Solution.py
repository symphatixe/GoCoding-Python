# Starter Code
scores = [50, 40, 60, 10, 70, 50, 50]


# Write your code below!

print("Original Scores: " + str(scores))
for num in range(len(scores)):
   scores[num] += 30

print("Hacked Scores: " + str(scores))

scores[1] += 20
scores[3] += 50
print("Hacked Scores: " + str(scores))