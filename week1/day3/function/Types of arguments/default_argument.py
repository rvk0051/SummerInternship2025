# 1. Default Arguments

# A default argument is a parameter that assumes a default value
# if a value is not provided in the function call for that argument.

# Example:-
# Python program to demonstrate
# default arguments
def example_function(x, y=50):
# 50 is the default argument for the parameter y.
    print("x: ", x)
    print("y: ", y)

example_function(10)
# calling a function with only one argument

#Output:-