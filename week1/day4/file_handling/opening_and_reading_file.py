
'''
Opening and Reading Files in Python

This script demonstrates different ways to open and read files in Python.
Key concepts covered:
1. Opening files using the 'with' context manager
2. Reading files in text mode
3. Reading files in binary mode
4. File operations and proper closing

File Modes:
- 'r': Read (text mode) - default mode
- 'rb': Read (binary mode)
- 'w': Write (text mode)
- 'wb': Write (binary mode)
- 'a': Append (text mode)
- 'ab': Append (binary mode)
'''

# Opening file in binary mode ('rb')
# Binary mode is useful for non-text files (images, PDFs, etc.)

file = open("python.txt", "rb")
content = file.read()  # Read the entire contents in binary mode
print(content)
file.close()  # closing the file
# Output: b'Hello World\r\n123456'

# With Statement
# with statement is used for resource management.
# It ensures that file is properly closed after its suite finishes,
# even if an exception is raised. with open()
# as method automatically handles closing the file once the block of code is exited,
# even if an error occurs.
# This reduces the risk of file corruption and resource leakage.

# opening file using 'with' statement

with open('python.txt', 'r') as file: # 'file' is a variable storing content of the file read
    # 'r' specifies read-only text mode
    contents = file.read() # Read the entire contents of the file
    print(contents)
    # Output:
    # Hello World
    # 123456

# Note: file.close() is not needed here as 'with' statement handles it automatically