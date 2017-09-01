# This exercise is for list comprehension
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

x = [1,2,5]
y = [5,10,15]
my_list = [for a in x for b in y if a==b]
print (my_list)
