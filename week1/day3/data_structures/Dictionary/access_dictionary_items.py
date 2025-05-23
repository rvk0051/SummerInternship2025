# Accessing dictionary Items
'''
We can access a value from a dictionary by using the key within square brackets or get()method.
'''
 # Example:
dict = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(dict["name"]) # Output: Alice

# Access using get()
print(dict.get("name")) # Output: Alice