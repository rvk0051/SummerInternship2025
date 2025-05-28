
# Creating a package:-
'''
1. How to Create and Access Packages in Python
Create a Directory
Make a directory for your package. This will serve as the root folder of your package.

2. Add Modules
Add Python files (.py files) to this directory. Each file is a module containing related functions, classes, or variables.

3. Include __init__.py
Add an __init__.py file inside the directory. This file can be empty, but it is required (in Python <3.3) to mark the directory as a package. It can also contain initialization code.

4. Add Sub-packages (Optional)
Create subdirectories inside the main package, each with their own __init__.py file. These act as sub-packages.

5. Import Modules
Use dot notation to import, e.g., from mypackage.module1 import greet.
'''

# for example, I have created a package named my_package and added 2 modules in it named 'greeting' and 'math_operations'.
# so now, I can import those modules

from my_package import greeting

# calling the function 'say_hello()' from the 'greeting' module in 'my_package' package
print(greeting.say_hello("Alice"))

# Output:- Hello, Alice!