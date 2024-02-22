# Gues a number and then dice is rlled. If output matches your guess, you Win
import random

print("We are going to roll a dice")
guess = int(input("Guess a dice roll (between 1 and 6) : \n"))
roll = random.randint(1, 6)
print("You guessed " + str(guess) + " and dice rolled to be " + str(roll) + ".", end="")
if (guess == roll):
    print("You guessed right.")
else:
    print("You guessed wrong.")