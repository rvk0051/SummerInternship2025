'''
Polymorphism in Functions:-

Duck typing enables functions to work with any object regardless of its type.

# Duck typing:- Duck Typing is a type system used in dynamic languages.
                For example, Python, Perl, Ruby, PHP, Javascript, etc.
                where the type or the class of an object is less important than the method it defines.
'''


# Example:-

def add(a, b):
    return a + b   # adds 'a' and 'b', regardless of their type.

print(add(3, 4))           # Integer addition
# Output: 7

print(add("Hello, ", "World!"))  # String concatenation
# Output: Hello, World!

print(add([1, 2], [3, 4])) # List concatenation
# Output: [1, 2, 3, 4]

# Here, the 'add' function works with all types of parameters regardless of it's data type.
# That's why 'add' follows polymorphism.

# print(add("a",4))   # Error:- both arguments should be of same type