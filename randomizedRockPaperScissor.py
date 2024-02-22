# A simple illustration of single player Rock-paper-scissor
import random

print("\n\n\nLet's witness a rock-paper-scissor game.\n\n")
    
print("\n\n\t\t\t\t\tROCK-PAPER-SCISSOR\n\n")

i = 0
countWon = 0
flag = 0

while (True): 
    i += 1
    print("\n\nRound " + str(i) + "\n\n")
    
    user1 = random.choice(['SCISSOR', 'PAPER', 'ROCK'])
    user2 = random.choice(['SCISSOR', 'PAPER', 'ROCK'])
    if (user1 == user2):
        flag = 0
    elif ((user1 == 'SCISSOR' and user2 == 'PAPER') or (user1 == 'PAPER' and user2 == 'ROCK') or (user1 == 'ROCK' and user2 == 'SCISSOR')):
        flag = 1
    else:
        flag = -1

    
    print("User 1 selected " + str(user1) + " and User 2 selected " + str(user2) + ".")
    
    if (flag == 1):
        print("USER 1 WON.")
        countWon += 1
    elif (flag == 0):
        print("Its a DRAW.")
    else :
        print("USER 2 WON.")

    l = input("\n\nEnter 'q' to quit Or Enter any otehr alphabet character to be here : ")
    if (l.strip() == 'q'):
        break
    
print("\n\nUSER 1 won %d times and USER 2 won %d out of %d times." %(countWon, i-countWon, i) )