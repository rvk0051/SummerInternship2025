#For Loops
#For loops are used for sequential traversal.
#For example: traversing a list or string or array etc.
# In Python, there is "for in" loop which is similar to foreach loop in other languages.

#Syntax:
#for iterator_var in sequence:
#    statements(s)

#Example:
number = 4
for i in range(0, number):
    print(i)
#This code prints the numbers from 0 to 3 (inclusive) using
#a for loop that iterates over a range from 0 to n-1 (where n = 4).
#Output:
# 0
# 1
# 2
# 3


#We can use for loop to iterate lists, tuples, strings and dictionaries in Python.
list = ["In", "Time", "Tec"]
for i in list:
    print(i)
#Output:-
#In
#Time
#Tec


#Iterating by the Index of Sequences
#We can also use the index of elements in the sequence to iterate.
#The key idea is to first calculate the length of the list and in iterate over the sequence within the range of this length.

length = len(list)
for index in range(length):
    print(list[index])

else:
    print("Inside Else Block")
#Using else Statement with for Loop
#We can also combine else statement with for loop like in while loop.
#But as there is no condition in for loop based on which the execution will terminate
#so the else block will be executed immediately after for block finishes execution.

#Output:-
#In
#Time
#Tec
#Inside Else Block