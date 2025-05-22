# Removing Elements from List

# We can remove elements from a list using:
# 1. remove(): Removes the first occurrence of an element.
# 2. pop(): Removes the element at a specific index or the last element if no index is specified.
# 3. del statement: Deletes an element at a specified index.

# Example:
example_list = [10, 20, 30, 40, 50]

print("Original list:", example_list)

# Removes the first occurrence of 30
example_list.remove(30)
print("After remove(30):", example_list)

# Removes the element at index 1 (which is now 20, after 30 was removed)
popped_val = example_list.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", example_list)

# Deletes the first element (which is now 10, after 20 was removed)
del example_list[0]
print("After del my_list[0]:", example_list)

#Output:
# After remove(30): [10, 20, 40, 50]
# Popped element: 20
# After pop(1): [10, 40, 50]
# After del a[0]: [40, 50]