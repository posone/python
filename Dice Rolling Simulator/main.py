from random import randint
import time

def RollDice():
    RANDOM_NUMBER = randint(1,6)
    print("Rolling...")
    time.sleep(2)
    print("The number which has been chosen", RANDOM_NUMBER)

while True:
    print("Welcome to the DiceRollingSimulator! What do you want to do?\n"
          "1) Roll the Dice!"
          "2) Quit")
    USERINPUT = input("Enter your choice:")
    if USERINPUT == '1':
        print(USERINPUT)
    if USERINPUT == '2':
        exit('Bye!')
        break
    else:
        print("Wrong choice, try again!")


