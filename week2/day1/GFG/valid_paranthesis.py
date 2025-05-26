'''

Checking Valid Parenthesis in Expression

Problem Statement:
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.

Example:

1.
Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.

2.
Input: s = "([]"
Output: False
Explanation: The expression is not balanced as there is a missing ')' at the end.

Solution:
solution function is 'isBalanced()'
'''

#Python program to check if parentheses are balanced
def isBalanced(s):

    # Declare a stack to store the opening brackets
    stack = []

    for i in range(len(s)):

        # Check if the character is an opening bracket
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])

        else:
            # If it's a closing bracket, check if the stack is non-empty
            # and if the top of the stack is a matching opening bracket
            if stack and ((stack[-1] == '(' and s[i] == ')') or
                       (stack[-1] == '{' and s[i] == '}') or
                       (stack[-1] == '[' and s[i] == ']')):

                # Pop the matching opening bracket
                stack.pop()
            else:
                # Unmatched closing bracket
                # or the stack is empty when we are remained with closing bracket.
                return False

    # If stack is empty, return True (balanced), otherwise False
    return not stack

# Time Complexity: O(n)
# Space Complexity: O(n)