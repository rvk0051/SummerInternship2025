# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# When the condition becomes false, the line immediately after the loop in the program is executed.

#Syntax:-
#while expression:
#    statement(s)

#Example:-
count = 0
while (count < 3):
    count = count + 1
    print("Hello")

#Output:-
#Hello
#Hello
#Hello


#else in while loop
#Else clause is only executed when our while condition becomes false.
#If we break out of the loop or if an exception is raised then it won't be executed.

#Syntax:-
#while condition:
     # execute these statements
#else:
     # execute these statements

#Example:-
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello")
else:
    print("In Else Block")
#The code prints "Hello" three times using a 'while' loop and
#then after the loop it prints "In Else Block" because there is an "else" block associated with the 'while' loop.
#Output:-
#Hello
#Hello
#Hello
#In Else Block