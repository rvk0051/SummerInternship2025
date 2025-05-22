# Positional arguments

# We used the Position argument during the function call
# so that the first argument is assigned to first parameter
# and the second argument is assigned to second parameter.

#Example:-
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

#Case 1:
# get correct output because
# argument is given in correct order
print("Case 1")
nameAge("Suraj", 27)
# 'Suraj' is assigned to name (first parameter) and 27 is assigned to age (second parameter)

#Case 2
#By changing the position, or if you forget the order of the positions, the values can be used in the wrong places.
print("Case 2")
nameAge(27, "Suraj")
# 27 is assigned to the name and Suraj is assigned to the age.

#Output:-
#Case 1
#Hi, I am Suraj
#My age is  27
#Case 2
#Hi, I am 27
#My age is  Suraj