# Python Tuples
# Tuples can contain elements of various data types, including other tuples, lists, dictionaries and even functions.

# Creating a Tuple with Mixed Datatype
tup = (5, 'abc', 7, 'xyz')
print(tup)  # Output:- (5, 'Welcome', 7, 'Geeks')

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('Data', 'Structures')
tup3 = (tup1, tup2)
print(tup3)  # Output:- ((0, 1, 2, 3), ('Data', 'Structures'))

# Creating a Tuple with repetition
tup1 = ('Data',) * 3
print(tup1)  # Output:- ('Data', 'Data', 'Data')

# Creating a Tuple with the use of loop
tup = ('Data')
for i in range(4):
    tup = (tup,)
    print(tup)
# Output:- ('Data',)
#          (('Data',),)
#          ((('Data',),),)
#          (((('Data',),),),)