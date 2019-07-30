# Program to simulate a random number generator with dice.
# Output will be a number between 1 and 6
# Project idea taken from https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
#
# ##### Dice Rolling Simulator #####
#
# The Goal: Like the title suggests, this project involves writing a
# program that simulates rolling dice. When the program runs, it will
# randomly choose a number between 1 and 6. (Or whatever other integer
# you prefer — the number of sides on the die is up to you.) The
# program will print what that number is. It should then ask you if
# you’d like to roll again. For this project, you’ll need to set the
# min and max number that your dice can produce. For the average die,
# that means a minimum of 1 and a maximum of 6. You’ll also want a
# function that randomly grabs a number within that range and prints
# it.
import random
userinput = "y"
while (userinput != "n"):
    print(random.randrange(1,6))
    userinput = input("Do you want to play again? [Y/n] ")
