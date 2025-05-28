# Using 'from' statement
'''
Python's 'from' statement lets you import specific attributes from a module without importing the module as a whole.
'''

# Example:-

# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial

# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))  # Output:- 4.0
print(factorial(6))  # Output:- 720