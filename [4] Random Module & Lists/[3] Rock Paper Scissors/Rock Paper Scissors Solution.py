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

match computer:
    case 1:
        computerChoice = rock
    case 2:
        computerChoice = paper
    case 3:
        computerChoice = scissors

match user:
    case 1:
        userChoice = rock
    case 2:
        userChoice = paper
    case 3:
        userChoice = scissors
    case _:
        print("Invalid input")
        exit()


match(user, computer):
    case(_, _) if user == computer:
        print(userChoice + "\n" + computerChoice)
        print("You have tied the computer, good job!")
    case(1, _):
        print(userChoice + "\n" + computerChoice)
        print("You chose rock, the computer chose paper. You have failed."
            if computer == 2
            else "You chose rock, the computer chose scissors. Congratulations on squashing the computer!")
    case(2, _):
        print(userChoice + "\n" + computerChoice)
        print("You chose paper, the computer chose scissors. You have failed."
            if computer == 3
            else "You chose paper, the computer chose rock. Congratulations on covering the computer!")
    case(3, _):
        print(userChoice + "\n" + computerChoice)
        print("You chose scissors, the computer chose rock. You have failed."
            if computer == 1
            else "You chose scissors, the computer chose paper. Congratulations on cutting up the computer!")