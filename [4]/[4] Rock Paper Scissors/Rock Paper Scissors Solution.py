# Starter Code
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below!
computer = random.randint(1, 3)
user = int(input("Hello, welcome to rock, paper, scissors, the classic game. Pick a number 1 - 3 and challenge the computer. \n"))

computerChoice = ""
userChoice = ""


if (computer == 1):
    computerChoice = rock
elif (computer == 2): 
    computerChoice = paper
else:
    computerChoice = scissors
    
if (user == 1):
    user = rock
elif (user == 2): 
    userChoice = paper
else:
    userChoice = scissors
    
    

if (user != 1 and user != 2 and user != 3):
    print("Invalid input, try again.")
    exit()
    
else:
    if (user == computer):
        print(userChoice + "\n" + computerChoice)
        print("You have tied the computer, good job!")
    elif(user == 1):
        if (computer == 2):
            print(userChoice + "\n" + computerChoice)
            print("You chose rock, the computer chose paper. You have failed.")
        else:
            print(userChoice + "\n" + computerChoice)
            print("You chose rock, the computer chose scissors. Congratulations on squashing the computer!")
            
    elif(user == 2):
        if (computer == 1):
            print(userChoice + "\n" + computerChoice)            
            print("You chose paper, the computer chose rock. Congratulations on covering the computer!")
        else:
            print(userChoice + "\n" + computerChoice)    
            print("You chose paper, the computer chose scissors. You have failed.")
            
    else:
        if (computer == 1):
            print(userChoice + "\n" + computerChoice)        
            print("You chose scissors, the computer chose rock. You have failed.")
        else:
            print(userChoice + "\n" + computerChoice)        
            print("You chose scissors, the computer chose paper. Congratulations on cutting up the computer!")