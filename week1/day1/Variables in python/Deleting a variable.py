#We can remove a variable from the namespace using the del keyword.
#memory used by the variable gets free.

x = 10
print(x)

# Removing the variable using del
del x

# Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise error