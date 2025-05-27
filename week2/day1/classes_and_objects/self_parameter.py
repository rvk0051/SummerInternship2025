'''
'self' parameter:-

'self' represents the instance of the class being used.
Whenever we create an object from a class, self refers to the current object instance.
It is essential for accessing attributes and methods within the class.

'''

# Example:-
class Number:
    def __init__(self, value):
        self.value = value

    # 'self' represents the instance of class 'Number'
    def print_value(self):
        print(self.value)


obj1 = Number(17)
obj1.print_value()
# Output:- 17

'''
Is "self" a Keyword?
Although self is not a Python keyword, using it is a widely accepted convention. 
This makes the code easier to read and understand for other developers, 
as it follows the general structure of object-oriented programming.

'''

# Example:-
class Color:
    def __init__(this, color):
        this.color = color

    def show(this):  # this represents the instance of class 'Color'
        print("Color is", this.color, ".")

# using 'this' instead of 'self'
color1 = Color("blue")
color1.show()
# Output:- Color is blue .

'''
'self': Pointer to the Current Object instance.:-

When we create an instance of a class, self points to the current object. 
It allows us to refer to the instance's attributes and methods. 
Every object created from a class will have its own self.

'''
# Example:-
class Address:
    def __init__(self):
        print("Address of self = ", id(self))
        # id() is used to know the unique memory address of the object passed.

object1 = Address()
print("Address of class object = ", id(object1))

# Output:- Address of self =  2627371474896
#          Address of class object =  2627371474896
# 'self' refers to the object created, that's why address of self and address of object is same.
