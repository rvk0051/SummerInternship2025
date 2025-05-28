# Renaming a module:-
'''
To rename a module, we could make an alias when import an module, using 'as' keyword.
'''

import calculate as calc  # importing  module 'calculate' and renaming it as 'calc' using 'as' keyword.

print(calc.add(1, 2))  # Calling function 'add' present in module 'calculate' and printing the output.
# Output:- 3