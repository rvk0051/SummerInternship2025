# Keyword Arguments:-

# The idea is to allow the caller to specify the argument name with values
# so that the caller does not need to remember the order of parameters.

# Python program to demonstrate Keyword Arguments
def greet(firstword, secondword):
    print(firstword, secondword)
greet(firstword='Good', secondword='Morning')
# This way the order of the arguments does not matter.
greet(secondword='Morning', firstword='Good')

# Output:-
# Good Morning
# Good Morning

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.