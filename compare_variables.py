# Assume that two variables, varA and varB, are assigned values, either
# numbers or strings.
# 
# Write a piece of Python code that evaluates varA and varB, and then
# prints out one of the following messages:
# 
# "string involved" if either varA or varB are strings
# 
# "bigger" if varA is larger than varB
# 
# "equal" if varA is equal to varB
# 
# "smaller" if varA is smaller than varB

varA = 'wind'
varB = 'ehllo'
# print (type(varA))
if (type(varA) == str) or (type(varB) == str):
    print("string involved")
if (type(varA) == type(varB)):
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")
