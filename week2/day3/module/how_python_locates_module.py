# How python locates modules?
'''
Python has a well-defined process for locating modules when you use an import statement.
This process involves searching through a specific list of directories in a particular order.
This list of directories is accessible through the sys.path variable.
'''

# The order in which Python searches for modules:
'''
1. The Directory of the Input Script (or Current Working Directory):

If you're running a Python script (e.g., python my_script.py), 
the directory containing my_script.py is the first place Python looks for modules.
If you're using the Python interpreter interactively, 
the current working directory (where you launched the interpreter) is the first search path.

2. PYTHONPATH Environment Variable:

Python then checks for an environment variable named PYTHONPATH.
If PYTHONPATH is set, it contains a list of directories 
(separated by colons on Unix-like systems and semicolons on Windows) that Python should also search. 
These directories are added to sys.path.
This is a way for users to tell Python to look in specific, non-standard locations for their modules.

3. Standard Library Directories:

Next, Python searches its standard library directories. 
These are where all the built-in modules (like os, sys, math, platform, etc.) are located. 
The exact path depends on your Python installation and operating system.

4. site-packages Directory:

Finally, Python checks the site-packages directory (or directories, as there can be multiple). 
This is the default location where third-party packages installed via pip (e.g., numpy, pandas, requests) are stored.
'''

#The sys.path List:
'''
The sys.path variable is a list of strings representing the directories that Python searches for modules.
'''

import sys
import pprint # For pretty printing long lists

print("Python's module search path (sys.path):")
pprint.pprint(sys.path)  # prints a list of strings representing the directories that Python searches for modules.