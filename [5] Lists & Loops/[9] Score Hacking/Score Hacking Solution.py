# Starter Code
scores = [50, 40, 60, 10, 70, 50, 50]


# Write your code below!
print(f"Original Scores: {scores}")
for num in range(len(scores)):
   scores[num] += 30

print(f"Hacked Scores: {scores}")

scores[1] += 20
scores[3] += 50
print(f"Hacked Scores: {scores}")