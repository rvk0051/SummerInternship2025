#A dictionary in Python is a collection of data values, used to store data values like a map,
#unlike other Python Data Types that hold only a single value as an element,
#a Dictionary holds a key: value pair. Key-value is provided in the dictionary to make it more optimized.
#Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.

#Values in a dictionary can be of any datatype and can be duplicated,
#whereas keys can’t be repeated and must be immutable.
#The dictionary can also be created by the built-in function dict().

# initialize empty dictionary
d = {}


d = {1: 'In', 2: 'Time', 3: 'Tec'}
print(d) #Output:- {1: 'In', 2: 'Time', 3: 'Tec'}

# creating dictionary using dict() constructor
d1 = dict({1: 'In', 2: 'Time', 3: 'Tec'})
print(d1) #Output:- {1: 'In', 2: 'Time', 3: 'Tec'}

#In order to access the items of a dictionary refer to its key name.
#Key can be used inside square brackets.
print(d[2]) #Accessing an element using key

#Using get() method we can access the dictionary elements.
print(d.get(3)) # Accessing a element using get