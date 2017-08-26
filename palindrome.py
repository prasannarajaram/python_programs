# Get an input string and verify if it is a palindrome or not
# To make this a little more challenging:
#  - Take a text input file and search for palindrome words
#  - Print if any word is found.

text = raw_input("Enter the string: ")
reverse = text[::-1]
if (text == reverse):
    print ("Palindrome")
else:
    print ("Not Palindrome")
