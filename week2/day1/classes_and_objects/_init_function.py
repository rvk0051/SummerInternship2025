'''

__init__ function

All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created

The __init__() function is called automatically every time the class is being used to create a new object.

'''

#Example:-
# Creating a class named 'Person', and using the __init__() function to assign values
# to 'name' and 'age' of the object when created.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person1 = Person("John", 36) # creating object 'person1' with passing values 'John' and 36
# so that these values gets passed to __init__ function and values will be assigned to the attributes of the object.

print(person1.name) # display name and age of the object 'person1' of class 'Person'
print(person1.age)

#Output:
# John
# 36
