# Accessing a Set in Python
# We can loop through a set to access set items as set is unindexed and
# do not support accessing elements by indexing.
# Also we can use in keyword which is membership operator to check if an item exists in a set.

set1 = set(["In", "Time", "Tec"])

# Accessing element using For loop
for i in set1:
    print(i, end=" ")
print()    # sets are unordered, the order of items printed is not guaranteed

# Checking the element using in keyword
print("Time" in set1)  # This checks if "Time" is in set1 or not, and prints boolean value.

# Output:
#In Time Tec
#True