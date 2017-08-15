# Exercise 1 (and Solution)
# 
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# 
# Extras:
# 
# - Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#   (Hint: order of operations exists in Python)
# - Print out that many copies of the previous message on separate lines.
#   (Hint: the string "\n is the same as pressing the ENTER button)
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

name = raw_input("Name: ")
age = int(input("Enter your age: "))
x = 100 - age
today = datetime.datetime.now()
y100 = today.year + x

#print (today.year)
# x = 100 - age
# today.year + x -> 100 years old
print ('Hello %s, You will be 100 years in %d'%(name,y100))

# Lessons learnt:
# 1. Import datetime module. This is one way to access the date and time info.
# 2. Print statement: Failed so many times until the above code was reached.
# 3. For strings the input() function does not work. Use raw_input() function

