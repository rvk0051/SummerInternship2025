# User-defined Exceptions:-
'''
User-defined exceptions are created by defining a new class
that inherits from Python's built-in Exception class or one of its subclasses.
By doing this, we can create custom error messages and handle specific errors in a way
that makes sense for our application.
'''

# Creating a user-defined exception:-
'''
To create a user-defined exception, create a new class that inherits from Exception or any of its subclasses.
'''

# Example:-

# Creating a custom exception class i.e.; user-defined exception 'InvalidAgeError'
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be above 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)  # 'super' is for parent class 'Exception'

    def __str__(self):
        return f'{self.message}'  # if this exception is raised, message will be displayed.

# defining class 'Person'
class Person:
    def __init__(self, age):
        self.age = age

    def valid_age_to_vote(self):
        if self.age < 18:
            raise InvalidAgeError(self.age)  # Raises exception if age > 18
        else:
            print(f"{self.age} is a valid age to vote.")


age = int(input("Enter age: "))
person = Person(age)   # creating object of class 'Person' with age as parameter.
try:
    person.valid_age_to_vote()  # Calls 'valid_age_to_vote' function

except InvalidAgeError as exception:   # if 'InvalidAgeError' exception is raised, this block will be executed
    print(exception)

# Output1:-
# Enter age: 15
# Age must be above 18

# Output2:-
#Enter age: 19
#19 is a valid age to vote.