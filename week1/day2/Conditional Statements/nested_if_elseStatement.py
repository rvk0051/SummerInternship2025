#Nested if-else Statements in Python
#Nested if..else means an if-else statement inside another if statement.
#We can use nested if statements to check conditions within conditions.
#Example:-
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
#Output:- 30% senior discount!