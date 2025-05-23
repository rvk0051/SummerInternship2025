'''
join() Function

This method is used to join a sequence of strings with some operator.
The join() operator will create a new string by joining
every character of the sequence with a specified character, including whitespaces.

Note: The join() method only accepts strings.
      If any element in the iteration is of a different type, an error will be thrown.


Syntax:

"character".join(seq)

character: The character from which the strings will be joined.
seq: Sequence of the strings to be joined.

'''
# Example:

string = 'String Manipulation'

# joining the above-given characters of the string with ‘,’.
string = ",".join(string)

print(string)
# Output:  S,t,r,i,n,g, ,M,a,n,i,p,u,l,a,t,i,o,n