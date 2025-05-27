'''
super() function:-

super() function is used to call the parent class’s methods.
In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes.

'''

class Person:  # Creating a class 'Person', with 'name' attribute, and a 'print_name' method
  def __init__(self, name):
    self.name = name

  def print_name(self):
    print(f"Hello, {self.name}")

class Student(Person):  #Creating a class 'Student', which inherits the 'Person' class
  def __init__(self, name, number):
    super().__init__(name)  # using super() function to call __init__ function of parent class 'Person'
    self.number = number  # adding attribute 'number' in the 'Student' class

# 'number' is not an attribute of 'Parent' class.

# Creating an instance of 'Student'
student1 = Student("Ram",46)

# 'number' - attribute of 'Student'
# 'name' - attribute of parent class, hence of the child class (Student) also.

print(student1.number)  # Output: 46  
student1.print_name()   # Output: Hello, Ram