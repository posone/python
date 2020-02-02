from random import randint
import time

def Roll():
    global RAND_NUMBER
    RAND_NUMBER = randint(0,10)
    print("The randomly number is:",RAND_NUMBER)

STATUS = True

while STATUS:
    print("Welcome to the Guess the Number!\n"
          "Choose your number from 0-10 and see if you have luck this time!")
    try:
        USER_INPUT = int(input("Enter your number:"))
    except ValueError:
        print("It is not a digit! Please enter a digit in a range 0-10")
    else:
        Roll()
        if USER_INPUT == RAND_NUMBER:
            print("You got it! You have won!")
            exit("The game is over, thank you for playing")
        if USER_INPUT > 10:
            print("Please choose the proper number! Only from 0-10.")
        else:
            print("Ahh, you have missed that, try again.")
