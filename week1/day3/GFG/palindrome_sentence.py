# Palindrome Sentence
# Given a single string s, the task is to check if it is a palindrome sentence or not.
# A palindrome sentence is a sequence of characters, such as word, phrase, or series of symbols
# that reads the same backward as forward after converting all uppercase letters to lowercase and
# removing all non-alphanumeric characters.

# Example:
# Input: s = "Abc 012..## 10cbA"
# Output: true
# Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase,
# string s will become “abc01210cba” which is a palindrome.

#code:
# solution to 'Palindrome Sentence' is the below function which is taking a string 's' as parameter
def sentencePalindrome(self, s):
    # your code here
    length = len(s)
    # Using two-pointer technique
    right = length - 1
    left = 0
    # Compares character until they are equal
    while left < right:
        #checking if the s[right] is alphanumeric
        if not s[right].isalnum():
            right -= 1
        # checking if the s[left] is alphanumeric
        elif not s[left].isalnum():
            left += 1
        # if the characters are equal, updating the pointers
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        # if characters are not equal, it string can't be a palindrome
        else:
            return False
    # Return true as sentence is palindrome
    return True

# Time Complexity:- O(n)   # due to while loop
# Space complexity:- O(1)