#Type casting refers to the process of converting the value of one data type into another. Python provides several built-in functions to facilitate casting
#Casting functions are used to convert data from one type to another.
'''
Some common casting functions are
Function      Converts to
int()          Integer
float()        Float
str()          String
bool()         Boolean
list()         List
tuple()        Tuple
set()          Set
'''

# using type() function, we can get the data type of a variable
numberS="10"
number=int(numberS) # Casts string to integer
print(type(number)) #output:- <class, 'int'>

list1=list(numberS) # Casts string to list
print(list1) #lis1=['1','0']
print(type(list1)) #output:- <class, 'list'>

tuple1=tuple(numberS) # Casts string to tuple
print(tuple1)  #tuple1=(1,0)
print(type(tuple1)) #output:- <class, 'tuple'>

set1=set(list1) #Casts list to set
print(set1) #set1={1,0}
print(type(set1)) #output:- <class, 'set'>