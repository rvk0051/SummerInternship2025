# Arbitrary Keyword Arguments

# Used when we don't know in advance how many positional arguments a function will receive.
# The *args syntax allows a function to accept a variable number of non-keyword arguments.
# These arguments are collected into a tuple inside the function.

# *args should be placed after any regular positional or default arguments.

# Example:-
def sum_all(*numbers): # 'numbers' is be a tuple
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))
# Output: 6

print(sum_all(10, 20, 30, 40, 50))
# Output: 150