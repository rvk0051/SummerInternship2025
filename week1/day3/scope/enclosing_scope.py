# Enclosing Scope

# This is used for nested functions.
# A function defined inside another function can access variables from its outer (enclosing) function.

#Example:-
def outer():
    var = 20
    # Enclosing scope for inner()
    def inner():
        print(var)
        # var is found in enclosing scope
    inner()
outer()  # Output:- 20

# inner()  # Gives error as it is in local cope of outer()