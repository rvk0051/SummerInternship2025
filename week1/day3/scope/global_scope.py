# Global Scope

# Names defined at the top-level of a script/module or
# declared global in a function.

# Example1:-
var = 30  # Global scope

def display():
    print(var) # var is accessible because it is a global variable

display()

#Output:- 30

# Example2:-

var = 100

def modify():
    global var # for referring to global 'var' not redefining one in local scope
    var = 200 # value of var gets modified

modify()
print(var)  # Output:- 200