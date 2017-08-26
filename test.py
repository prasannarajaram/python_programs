# num = 2
# for num in range(2,11,2):
#     print (num)
# print('Goodbye!')
#
# print('Hello')
# num = 10
# for num in range(10,1,-2):
#     print(num)
#
# end = 6
# ans = 0
# last = end + 1
# for num in range(0,last):
#     ans = ans + num
# print(ans)
# 
# Letter # 0 is S, Letter # 1 is n, Letter # 2 is o, Letter # 3 is w, Letter # 4 is !

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
