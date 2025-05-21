#Python programming language allows to use one loop inside another loop which is called nested loop.

#Syntax:
#for iterator_var in sequence:
#  for iterator_var in sequence:
#      statements(s)
#  statements(s)

#The syntax for a nested while loop statement in the Python programming language is as follows:
#while expression:
#   while expression:
#       statement(s)
#   statement(s)

#A final note on loop nesting is that we can put any type of loop inside of any other type of loops in Python.
#For example, a for loop can be inside a while loop or vice versa.
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()
#Output:
#1
#2 2
#3 3 3
#4 4 4 4