# Starter Code
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


# Write your code below!
choice1 = input("Pick a direction to go, left or right. \n").lower()

if (choice1 == "left"):
    choice2 = input("There is a small sewer in front of you, do you swim through it or wait? \n").lower()

    if (choice2 == "swim"): print("You are attacked by mutated trout, game over!")
    elif (choice2 == "wait"):
        choice3 = input("There are three doors in front of you, red, blue, and yellow. You can also choose to walk back. Choose between red, blue, yellow, and back. \n").lower()

        if (choice3 == "red"):
            print("You are burned by fire, game over!")
        elif (choice3 == "blue"):
            print("You are eaten by monsters, game over!")
        elif (choice3 == "yellow"):
            print("You found the treasure!")
        else:
            print("You chose to walk back or wait, a huge rock falls from the top and crushes you, game over!")

    else: print("You did not wait or swim through the water, the sewer got flooded with water!!!")


elif (choice1 == "right"): print("You fell into a hole, game over!")
else: print("You waited too long and a spike trap appeared under you!")