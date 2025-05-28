# Module in python
'''
A Python module is a file containing Python definitions and statements.
A module can define functions, classes, and variables. A module can also include runnable code.

Grouping related code into a module makes the code easier to understand and use.
It also makes the code logically organized.

'''

# Create a python module:-
'''
To create a module just save the code you want in a file with the file extension .py.

Example:-
# A simple module, calculate.py
def add(x, y):
    return (x+y)

def subtract(x, y):
    return (x-y)
    
'''

# Import module in python:-
'''
We can import the functions, and classes defined in a module to another module using the import statement in some other Python source file.

When the interpreter encounters an import statement, it imports the module if the module is present in the search path.

Note: A search path is a list of directories that the interpreter searches for importing a module.

Syntax:- import module
'''
# Example:-
# I am making a file 'calculate.py', so that we can import it.


import calculate  # importing  module calculate.py

print(calculate.add(10, 2)) # Calling function present in module 'calculate' and printing the output.
# Output:- 12
