# Adding elements to a list

# We can add elements to a list using the following methods:
# 1. append(): Adds an element at the end of the list.
# 2. extend(): Adds multiple elements to the end of the list.
# 3. insert(): Adds an element at a specific position.

# Example:

# Initialize an empty list
list1 = []

# Adding 10 to end of list
list1.append(10)
print("After append(10):", list1)
# Output: After append(10): [10]

# Inserting 5 at index 0
list1.insert(0, 5)
print("After insert(0, 5):", list1)
# Output: After insert(0, 5): [5, 10]

# Adding multiple elements  [15, 20, 25] at the end
list1.extend([15, 20, 25])
print("After extend([15, 20, 25]):", list1)
# Output: After extend([15, 20, 25]): [5, 10, 15, 20, 25]