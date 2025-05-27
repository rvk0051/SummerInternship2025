# Difference Between Exception and Error:-
'''

Error: Errors are serious issues that a program should not try to handle.
       They are usually problems in the code's logic or configuration and need to be fixed by the programmer.
       Examples include syntax errors and memory errors.

Exception: Exceptions are less severe than errors and can be handled by the program.
           They occur due to situations like invalid input, missing files or network issues.
'''

# Example:-

# Error
print("Hello world"  # Syntax error:- Missing closing parenthesis

# Exception
n = 10
res = n / 0  # ZeroDivisionError

# A syntax error is a coding mistake that prevents the code from running.
# In contrast, an exception like ZeroDivisionError can be managed during the program's execution using exception handling.