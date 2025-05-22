# Local Scope

# This is the innermost scope, inside a function or method.
# Names defined here are only accessible within that function.

#Example:-
def my_function():
  var = 300 # var is in local scope
  print(var)

my_function()
# print(var)  # Error! as var is in local scope of function ans is not accessible globally.

# Output:- 300