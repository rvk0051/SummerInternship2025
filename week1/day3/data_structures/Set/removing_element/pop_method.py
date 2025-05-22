#Using pop() Method
# pop() method removes and returns an arbitrary element from the set
# set is an unordered data structure, that's why
# there's no such way to determine which element is popped by using the pop() function.
# If the set is empty, it raises a KeyError.

# Example:
set1 = {1, 2, 3, 4, 5}
val = set1.pop()
print(val)
print(set1)

# Output:
#1
#{2, 3, 4, 5}