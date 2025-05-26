'''
Class attributes:
  These are the variables that are shared across all instances of a class.
  It is defined at the class level, outside any methods.
  All objects of the class share the same value for a class variable unless explicitly overridden in an object.

Instance Variables:
  Variables that are unique to each instance (object) of a class.
  These are defined within __init__ method or other instance methods.
  Each object maintains its own copy of instance variables, independent of other objects.
'''

# Example:

class Dog:
    # Class variable:  Shared by all instances of the class.
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables are defined in the __init__ method. Unique to each instance.
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Output: Canine
#         Buddy
#         Charlie


# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)
# Changing dog1.name only affects dog1 and does not impact dog2.
# Output: Max

# Modify class variable
Dog.species = "Feline"
# Changing Dog species affects all objects, as it's a property of the class itself.
print(dog1.species)  # (Updated class variable)
print(dog2.species)

# Output: Feline
#         Feline
