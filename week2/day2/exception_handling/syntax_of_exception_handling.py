# Syntax and Usage:-
'''
Exception handling in Python is done using the try, except, else and finally blocks.

try:
      # Code that might raise an exception
except SomeException:
      # Code to handle the exception
else:
     # Code to run if no exception occurs
finally:
    # Code to run regardless of whether an exception occurs

'''

# try, except, else and finally Blocks:-
'''
try Block: try block test a block of code for errors. 
           Python will "try" to execute the code in this block. 
           If an exception occurs, execution will immediately jump to the except block.

except Block: except block enables us to handle the error or exception. 
              If the code inside the try block throws an error, Python jumps to the except block and executes it. 
              We can handle specific exceptions or use a general except to catch all exceptions.

else Block: else block is optional and if included, must follow all except blocks. 
            The else block runs only if no exceptions are raised in the try block. 
            This is useful for code that should execute if the try block succeeds.

finally Block: finally block always runs, regardless of whether an exception occurred or not. 
               It is typically used for cleanup operations (closing files, releasing resources).
'''

# Example:-

divisor = int(input("Enter divisor: "))
try:  # It test if the the code in the block have exceptions or not.
    result = 100 / divisor

except ZeroDivisionError:  # It will run if 'try' block has 'ZeroDivisionError' exception.
    print("You can't divide by zero!")

else:  # It will execute if except block runs or not.
    print("Result is", result)

finally:  # It will execute regardless whether the try block has exception or not.
    print("Execution complete.")

# Output1:-
# Enter divisor: 0
# You can't divide by zero!
# Execution complete.

# Output2:-
# Enter divisor: 10
# Result is 10.0
# Execution complete.