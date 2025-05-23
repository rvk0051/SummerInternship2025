'''
Adding and Updating Dictionary Items
We can add new key-value pairs or update existing keys by using assignment.
'''
# Example:
dict = {1: 'In', 2: 'xyz', 3: 'abc'}

# Adding a new key-value pair
dict["number"] = 22

# Updating an existing value
dict[1] = "Python dict"

print(dict) # Output: {1: 'Python dict', 2: 'xyz', 3: 'abc', 'number': 22}
