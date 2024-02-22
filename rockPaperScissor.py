# A simple illustration of single player Rock-paper-scissor

import random

def selection(c):
    if (c == 's'):
        return "SCISSOR"
    if (c == 'r'):
        return "ROCK"
    if (c == 'p'):
        return "PAPER"
    



print("\n\n\t\t\t\t\tROCK-PAPER-SCISSOR\n\n")
print("INSTRUCTIONS: \n")
print("Enter 's' for SCISSOR, 'p' for PAPER and 'r' for ROCK\n")
print("Enter 'q' to quit\n\n\n")

i = 0
countWon = 0
flag = 0

while (True): 
    i += 1
    print("\n\nRound " + str(i) + "\n\n")
    you = input("Make your selection : ")
    if (you != 's' and you != 'r' and you != 'p' and you != 'q'):
        print("You made invalid selection. Please choose from 'p', 's', 'r' or 'q'.\n\n")
        i -= 1
        continue
    
    if (you == 'q'):
        i -= 1
        break

    comp = random.choice(['s', 'p', 'r'])
    if (you == comp):
        flag = 0
    elif ((you == 's' and comp == 'p') or (you == 'p' and comp == 'r') or (you == 'r' and comp == 's')):
        flag = 1
    else:
        flag = -1

    print("\nYou selected " + selection(you) + " and Computer selected " + selection(comp) + ".")
    
    if (flag == 1):
        print("YOU WON.")
        countWon += 1
    elif (flag == 0):
        print("Its a DRAW.")
    else :
        print("You LOST.")
    
print("\n\nYou won %d times out of %d" %(countWon, i))