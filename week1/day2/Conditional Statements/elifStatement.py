#elif statement in Python stands for "else if."
#It allows us to check multiple conditions,
#providing a way to execute different blocks of code based on which condition is true.
#Using elif statements makes our code more readable and efficient
# by eliminating the need for multiple nested if statements.

#Example:-
num1 = 33
num2 = 33
if num2 > num1:
  print("num2 is greater than num1")
elif num1 == num2:
  print("num1 and num2 are equal")
else:
    print("num1 is greater than num2")
#Output:-num1 and num2 are equal