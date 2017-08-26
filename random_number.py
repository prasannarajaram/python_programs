# Generate a random number between 1 and 9 (both inclusive)
# Ask user for a number between 1 and 9 and reply if they guessed
# too high, too low or exactly right.

import random
loop = "c"
while loop != "q":
    a = random.randint(1,9)
    print a
    loop = raw_input("Press Q to quit or return to continue: ")
    loop = loop.lower()
