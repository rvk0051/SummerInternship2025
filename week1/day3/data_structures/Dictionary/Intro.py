'''

A Python dictionary is a data structure that stores the value in key: value pairs.
Values in a dictionary can be of any data type and can be duplicated,
whereas keys can't be repeated and must be immutable.

Example: Here, The data is stored in key:value pairs in dictionaries,
which makes it easier to find values.

'''
dict1 = { 1: 'In', 2:'Time', 3:'Tec'}  # Declaring dictionary
# 1, 2, 3 are keys and 'In', 'Time', 'Tec' are the corresponding values
print(dict1) # Output: {1: 'In', 2: 'Time', 3: 'Tec'}

# create dictionary using dict() constructor
dict2 = dict(a = "In", b = "Time", c = "Tec")
print(dict2) # Output: {'a': 'In', 'b': 'Time', 'c': 'Tec'}