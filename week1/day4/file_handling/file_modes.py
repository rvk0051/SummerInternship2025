'''
File Modes in Python
When opening a file, we must specify the mode we want to which specifies what we want to do with the file.
Here’s a table of the different modes available:

Mode	           Description	                                                 Behavior

r	    Read-only mode.	                                        File must exist; otherwise, it raises an error.

rb	    Read-only in binary mode.	                            File must exist; otherwise, it raises an error.

r+	    Read and write mode.	                                File must exist; otherwise, it raises an error.

rb+	    Read and write in binary mode.	                        File must exist; otherwise, it raises an error.

w	    Write mode.	                                            Creates a new file or truncates the existing file.

wb	    Write in binary mode.	                                Creates a new file or truncates the existing file.

w+	    Write and read mode.	                                Creates a new file or truncates the existing file.

wb+	    Write and read in binary mode.	                        Creates a new file or truncates the existing file.

a	    Append mode.	                                        Creates a new file if it doesn't exist.

ab	    Append in binary mode.	                                Creates a new file if it doesn't exist.

a+	    Append and read mode.	                                Creates a new file if it doesn't exist.

ab+	    Append and read in binary mode.	                        Creates a new file if it doesn't exist.

x	    Exclusive creation mode.	                            Raises an error if the file already exists.

xb	    Exclusive creation in binary mode.	                    Raises an error if the file already exists.

x+	    Exclusive creation with read and write mode.	        Raises an error if the file exists.

xb+	    Exclusive creation with read and write in binary mode.	Raises an error if the file exists.
'''