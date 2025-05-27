'''
Inheritance in Python:-

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class
(called a child or derived class) to inherit attributes and methods from another class (called a parent or base class).
This promotes code reuse, modularity, and a hierarchical class structure.
'''

# Parent class
# Any class can be a parent class, so the syntax is the same as creating any other class.

# Example:
class Person:  # Creating a class 'Person', with 'name' attribute, and a 'print_name' method
  def __init__(self, name):
    self.name = name

  def print_name(self):
    print(self.name)


# Child class:
# To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class.

# Example:-
class Student(Person):  #Creating a class 'Student', which will inherit the properties and methods from the 'Person' class
  pass
# 'Student' class has the same properties and methods as the 'Person' class.

# Creating an instance of 'Student'
student1 = Student("Ram")  # 'student1' inherited property 'name' and method 'print_name' from parent class 'Person'
student1.print_name()
# Output:- Ram