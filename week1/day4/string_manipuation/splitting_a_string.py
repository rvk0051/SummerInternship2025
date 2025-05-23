'''
Split a String

It is a very common practice to split a string into smaller strings.
In Python, we use the split() function to do this.
It splits the string from the identified separator and returns all the pieces in a list.

Syntax:

string.split(separator, maxsplit)

separator: the string splits at this separator.
maxsplit (optional): tells how many splits to do.

'''
# For example,

string = 'Welcome to ITT'

# Splitting across the whitespace.
myList = string.split(" ")

print(myList)
# Output: ['Welcome', 'to', 'ITT']

# Note: The split() method, by default, takes any consecutive number of whitespaces as delimiters.