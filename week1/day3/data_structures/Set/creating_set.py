# Creating set

# In Python, the most basic and efficient method for creating a set is using curly braces.
# Example:
# set1 = {1, 2, 3, 4}
# print(set1)

# Using the set() function
# Python Sets can be created by using the built-in set() function with an iterable object or
# a sequence by placing the sequence inside curly braces, separated by a 'comma'.

#Note: A Python set cannot have mutable elements like a list or dictionary, as list and dictionary are immutable.

# Example:
# Creating a Set
set1 = set()
print(set1)   # Output: set()

# Creating set using set() function
set1 = set("InTimeTec")
print(set1)   # Output: {'I', 'T', 'c', 'm', 'i', 'n', 'e'}

# Creating a Set with the use of a List
set1 = set(["In", "Time", "Tec"])
print(set1)   # Output: {'Tec', 'In', 'Time'}

# Creating a Set with the use of a tuple
tup = ("In", "Time", "Tec")
print(set(tup))  # Output: {'Tec', 'In', 'Time'}

# Creating a Set with the use of a dictionary
dict = {"In": 1, "Time": 2, "Tec": 3}
print(set(dict))  # Output: {'Tec', 'In', 'Time'}
