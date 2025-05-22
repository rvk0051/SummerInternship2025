# remove() or discard()

# remove() method removes a specified element from the set.
# If the element is not present in the set, it raises a KeyError.

# discard() method also removes a specified element from the set.
# Unlike remove(), if the element is not found, it does not raise an error.


#Example:
# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  # Output: {1, 2, 4, 5}

# Using discard() Method
set1.discard(4)
print(set1)  # Output: {1, 2, 5}

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)  # Output: {1, 2, 5}