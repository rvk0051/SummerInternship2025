#Loop control statements change execution from their normal sequence.
#When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
#Python supports the following control statements:  1. Break  2. Continue  3. Pass


#Continue Statement
#The continue statement in Python returns the control to the beginning of the loop.
#The continue statement is used to skip the current iteration of a loop and move to the next iteration.
# It is useful when we want to bypass certain conditions without terminating the loop.

#Example:
for letter in 'intimetec':
    if letter == 'e' or letter == 'i':
        continue
    print('Current Letter :', letter)

#Output:
#Current Letter : n
#Current Letter : t
#Current Letter : m
#Current Letter : t
#Current Letter : c


#Break Statement
#The break statement in Python brings control out of the loop.
#Explanation: break statement is used to exit the loop prematurely when a specified condition is met.
#In this example, the loop breaks when the letter is either 'e' or 's', stopping further iteration.

#Example:
for letter in 'intimetec':
    if letter == 'e':
        break
    print('Current Letter :', letter)

#Output:
#Current Letter : t
#Current Letter : i
#Current Letter : m


#Pass Statement
#We use pass statement in Python to write empty loops.
#Pass is also used for empty control statements, functions and classes.
# In this example, the loop iterates over each letter in but doesn't perform any operation, and after the loop finishes, the last letter is printed.
#Example:
for letter in 'intimetec':
    pass
print('Last Letter :', letter)

#Output:
#Last Letter : c