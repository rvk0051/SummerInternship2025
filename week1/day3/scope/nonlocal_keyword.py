# Nonlocal Keyword

# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.

# Example:-
def func1():
  var = "Hi"
  def func2():
    nonlocal var # for referring to 'var' defined in func1
    var = "hello"  # and modifying the value of 'var'
  func2()
  return var

print(func1())  # Output:- hello