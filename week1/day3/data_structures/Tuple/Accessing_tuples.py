# Accessing Tuples
# We can access the elements of a tuple by using indexing and slicing, similar to how we access elements in a list.
# Indexing starts at 0 for the first element and goes up to n-1, where n is the number of elements in the tuple.
# Negative indexing starts from -1 for the last element and goes backward.

# Accessing Tuple with Indexing
tup = tuple("Time")
print(tup[0])  # Output: T

# Accessing a range of elements using slicing
print(tup[1:4]) # Output: ('i', 'm', 'e')
print(tup[:3])  # Output: ('T', 'i', 'm')

# Tuple unpacking
tup = ("In", "Time", "Tec")
# This line unpack values of Tuple1
word1, word2, word3 = tup
print(word1)
print(word2)
print(word3)
# Output:- In
#          Time
#          Tec