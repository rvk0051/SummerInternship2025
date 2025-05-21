#Else allows us to specify a block of code that will execute if the condition(s) associated with an if or elif statement
# evaluates to False. Else block provides a way to handle all other cases that don't meet the specified conditions.
#Example:-
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


#Short Hand if-else
#The short-hand if-else statement allows us to write a single-line if-else statement.
#Example:-
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")
