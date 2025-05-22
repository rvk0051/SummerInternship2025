# Anonymous Functions in Python
# In Python, an anonymous function means that a function is without a name.
# As we already know the def keyword is used to define the normal functions and
# the lambda keyword is used to create anonymous functions.

#Example:

def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x  # Anonymous function using lambda

print("Using function, ",cube(7))
print("Using lambda, ",cube_v2(7))

#Output:
#Using function,  343
#Using lambda,  343