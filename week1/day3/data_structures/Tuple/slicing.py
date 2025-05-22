# Slicing of a tuple
'''

Slicing a tuple means creating a new tuple from a subset of elements of the original tuple.
The slicing syntax is tuple[start:stop:step].

Note- Negative Increment values can also be used to reverse the sequence of Tuples.

'''
# Slicing of a Tuple with Numbers
tup = tuple('InTimeTec')

# Removing First element
print(tup[1:])  # Output: ('n', 'T', 'i', 'm', 'e', 'T', 'e', 'c')

# Reversing the Tuple
print(tup[::-1])  # Output: ('c', 'e', 'T', 'e', 'm', 'i', 'T', 'n', 'I')

# Printing elements of a Range
print(tup[4:9])  # Output: ('m', 'e', 'T', 'e', 'c')