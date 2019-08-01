# Guess the Number

# The Goal: Similar to the first project, this project also uses the
# random module in Python. The program will first randomly generate a
# number unknown to the user. The user needs to guess what that number
# is. (In other words, the user needs to be able to input
# information.) If the user’s guess is wrong, the program should
# return some sort of indication as to how wrong [e.g. The number is
# too high or too low]. If the user guesses correctly, a positive
# indication should appear.  You’ll need functions to check if the
# user input is an actual number, to see the difference between the
# inputted number and the randomly generated numbers, and to then
# compare the numbers

import random
number = random.randrange(1, 10)
userinput = 1
while userinput != 0:
    userinput = int(input("Guess a number between 1 and 10 (0 to Quit) "))
    if userinput == 0:
        break
    if number == userinput:
        print("You guessed it right!")
        break
    if number > userinput:
        print("Guess a little higher")
    else:
        print("Guess a little lower")
