#Match-Case Statement in Python
#match-case statement is Python's version of a switch-case found in other languages.
#Instead of writing many if-else statements, you can use the match statement.
#The match statement selects one of many code blocks to be executed.

#This is how it works:
#The match expression is evaluated once.
#The value of the expression is compared with the values of each case.
#If there is a match, the associated block of code is executed.

#Example:
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
#Use the underscore character _ as the last case value if you want a code block to execute
#when there are no other matches
  case _:
    print("Weekday")
#Output:- Weekday


#Combine values
#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case
#Example:-
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("Today is a weekend")
#Output:- Today is a weekday

#if in match-case statements
#if statements in the case evaluation can be added as an extra condition-check
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")