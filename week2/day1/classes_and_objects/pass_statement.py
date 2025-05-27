'''
The pass Statement:-

class definitions cannot be empty,
but if you for some reason have a class definition with no content,
put in the pass statement to avoid getting an error.

'''

class Person:  # created an empty class
# Output:-
# IndentationError: expected an indented block after class definition on line 10

class Person:
    pass  # used pass statement
# No error generated.