# Lists in Python

# In Python, a list is a built-in dynamic sized array (automatically grows and shrinks).
# We can store all types of items (including another list) in a list.
# A list may contain mixed type of items, this is possible because
# a list mainly stores references at contiguous locations and actual items maybe stored at different locations.

# 1. List can contain duplicate items.
# 2. List in Python are Mutable. Hence, we can modify, replace or delete the items.
# 3. List are ordered. It maintain the order of elements based on how they are added.
# 4. Accessing items in List can be done directly using their position (index), starting from 0.


# Creating a Python list with different data types
list1 = [10, 20, "abc", 40, True]

print(list1)  # Output: [10, 20, 'abc', 40, True]

# Accessing elements using indexing
print(list1[0])  # Output: 10
print(list1[1])  # Output: 20
print(list1[2])  # Output: "abc"
print(list1[3])  # Output: 40
print(list1[4])  # Output: True

# Checking types of elements
print(type(list1[2]))  # str
print(type(list1[4]))  # bool

#Note: Lists Store References, Not Values
# Each element in a list is not stored directly inside the list structure.
# Instead, the list stores references (pointers) to the actual objects in memory.

# The list a itself is a container with references (addresses) to the actual values.
# Python internally creates separate objects for 10, 20, "abc", 40 and True,
# then stores their memory addresses inside list1.
# This means that modifying an element doesn’t affect other elements
# but can affect the referenced object if it is mutable