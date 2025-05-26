'''
Classes in Python:-

A class in Python is a user-defined template for creating objects.
It bundles data and functions together, making it easier to manage and use them.
When we create a new class, we define a new type of object.
We can then create multiple instances of this object type.


Object:-

An Object is an instance of a Class.
It represents a specific implementation of the class and holds its own data.


Creating classes:-

Classes are created using class keyword.
Attributes are variables defined inside the class and represent the properties of the class.
Attributes can be accessed using the dot . operator (e.g., MyClass.my_attribute).

'''

# Example:

# Create a class
class Dog:
    sound = "bark"  # class attribute
    # 'sound' attribute can be shared across all instances of Dog class.

# Create an object from the class
dog1 = Dog()

# Access the class attribute
print(dog1.sound)  # Output: bark
