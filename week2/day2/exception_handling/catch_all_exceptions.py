'''
To catch any exception possible in 'try' block, we don't specify any exception,
so that any exception if is there in 'try' block, 'except' block will run.

Syntax:-
try:
      # Code that might raise an exception
except :                         # we didn't specify any exception
      # Code to handle the exception
'''

# Example:-
try:
    # Simulate risky calculation: incorrect type operation
    res = "100" / 20

except:
    print("Something went wrong!")

# Output:- Something went wrong!