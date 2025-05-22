# Concatenation of Strings

# Tuples can be concatenated using the + operator.
# This operation combines two or more tuples to create a new tuple.

# Note- Only the same datatypes can be combined with concatenation,
#       an error arises if a list and a tuple are combined.

# example:
tup1 = (0, 1, 2, 3)
tup2 = ('In', 'Time', 'Tec')
tup3 = tup1 + tup2
print(tup3)  # Output:- (0, 1, 2, 3, 'In', 'Time', 'Tec')