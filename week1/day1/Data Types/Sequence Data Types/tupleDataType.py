#Just like a list, a tuple is also an ordered collection of Python objects.
#The only difference between a tuple and a list is that tuples are immutable.
#Tuples cannot be modified after it is created.

#Creating a tuple in Python
#tuples are created by placing a sequence of values separated by a ‘comma’ with or without
#the use of parentheses for grouping the data sequence.
#Tuples can contain any number of elements and of any datatype (like strings, integers, lists, etc.).

tup1 = ()
print(tup1)
#Output:- ()

tup2 = ('Hi', 'team')
print(tup2)
#Output:- ('Hi', 'team')

#Note:  Tuples can also be created with a single element, but it is a bit tricky.
#Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.
tup3 = ('4',) #Tuple having only one element
print(tup3)
#Output:- ('4',)
print(type(tup3)) #Output:- <class 'tuple'>

tup4 =('4')
print(tup4)
#Output:- 4
print(type(tup4)) #Output:- <class 'string'>
#So, if we are having only one element in tuple and trailing 'comma' is not there, then tuple is not defined.