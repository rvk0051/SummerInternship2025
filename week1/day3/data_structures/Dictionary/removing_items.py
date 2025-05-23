'''
Removing Dictionary Items

We can remove items from dictionary using the following methods:
1. del: Removes an item by key.
2. pop(): Removes an item by key and returns its value.
3. clear(): Empties the dictionary.
4. popitem(): Removes and returns the last key-value pair.

'''

dict = {1: 'str1', 2: 'str2', 3: 'str3', 'number':22}

# Using del to remove an item
del dict["number"]
print(dict)  # Output: {1: 'str1', 2: 'str2', 3: 'str3'}

# Using pop() to remove an item and return the value
val = dict.pop(1)
print(val)  # Output: str1

# Using popitem to removes and returns
# the last key-value pair.
key, val = dict.popitem()
print(f"Key: {key}, Value: {val}")  # Output: Key: 3, Value: str3

# Clear all items from the dictionary
dict.clear()
print(dict)  # Output: {}