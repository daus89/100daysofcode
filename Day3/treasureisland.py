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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')

print(f"Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input('You\'re and a junction, please choose whether to go "right" or "left".').lower()

if choice1 == "left": #continue with the game
   choice2 = input('You\'ve come an island, would u like to "wait" for a boat and want to "swim"? ').lower()
   if choice2 == "wait": #continue the game
       choice3 = input(f'You\'ve come to an island with many doors, please choose door "yellow", "red" or "blue".')
       if choice3 == "yellow":
           print("You have found the treasure, you win!")
       elif choice3 == "red":
           print("You have fell into a hole. Game over!")
       elif choice3 == "blue":
           print("You choose the wrong door. You got eaten by a zombie. Game over!")
       else:
           print(" Game over!")    
   else:
       print(f"You are attacked by a group of angry trout. Game Over!")
else:
    print("You fell into a hole. Game over!")