'''
Iterating Through a Dictionary
We can iterate over keys [using keys() method] , values [using values() method]
or both [using item() method] with a for loop.
'''
# Example:
dict = {1: 'In', 2: 'Time', 3: 'Tec'}

# Iterate over keys
for key in dict:
    print(key)
#Output: 1
#        2
#        3

# Iterate over values
for value in dict.values():
    print(value)
# Output:
# In
# Time
# Tec

# Iterate over key-value pairs
for key, value in dict.items():
    print(f"{key}: {value}")
# Output:
# 1: In
# 2: Time
# 3: Tec