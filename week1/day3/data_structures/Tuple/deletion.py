'''
Since tuples are immutable, we cannot delete individual elements of a tuple.
However, we can delete an entire tuple using del statement.
'''

# Deleting a Tuple
tup = (0, 1, 2, 3, 4)
del tup
print(tup) # Printing of Tuple after deletion results in an Error.
#Output:
# NameError: name 'tup' is not defined