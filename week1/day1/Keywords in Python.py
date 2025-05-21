#Keywords in Python are reserved words that have special meanings and serve specific purposes in the language syntax.
# They cannot be used as identifiers (names for variables, functions, classes, etc.).
# For instance, "for", "while", "if", and "else" are keywords and cannot be used as identifiers.

#Below list of keywords could be seen

import keyword

# Prints the list of keywords
print(keyword.kwlist)

#Output:-
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Checks if a string is a keyword
word = "if"
if keyword.iskeyword(word):
    print(f"{word} is a keyword.")
else:
    print(f"{word} is not a keyword.")