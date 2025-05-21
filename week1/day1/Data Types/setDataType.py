#Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements.
# The order of elements in a set is undefined though it may consist of various elements.

#Sets can be created by using the built-in set() function with an iterable object or a sequence by placing
# the sequence inside curly braces, separated by a ‘comma’.
s1 = set()
print(s1) #output:- set()

s2 = set("InTimeTec")
print("Set with the use of String: ", s2)
#Output:- Set with the use of String:  {'e', 'I', 'T', 'n', 'c', 'i', 'm'}

s3 = set({"In", "Time", "In"})
print("Set with the use of List: ", s3)
#Output:- Set with the use of List:  {'In', 'Time'}

# The type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set.