# Print Anagrams Together
'''
Given an array of strings, return all groups of strings that are anagrams. The strings in each group must be arranged in the order of their appearance in the original array. Refer to the sample case for clarification.
'''
from collections import defaultdict

# Example1
'''
Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
'''

# Example2
'''
Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.
'''

# Solution function is 'anagrams'

# Approach1:-
def anagrams(self, arr):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''

    #Initializing resultant as an empty list.
    result = []

    length = len(arr)

    # if array has no element than result will be an empty list
    if length == 0:
        return result

    for word in arr:
        # checking each word in given array,

        found = False# Flag to keep track if an anagram group is found

        # Compare sorted characters of current word and the first word in the group.
        # If match found, add word to the group
        # Mark that anagram group is found
        for group in result:
            if sorted(word) == sorted(group[0]):
                group.append(word)
                found = True
                break

        # If no matching anagram group is found, create a new group with current word
        if not found:
            result.append([word])

    # Return the list of anagram groups
    return result

# here m is the average length of words, and
# n is the no. of words in 'arr'
# Time Complexity: O(n.mlogm), as sorting is done for each word.
# Space Complexity: O(n)

# Approach2:
'''
defaultdict(list): Creates a dictionary that automatically creates an empty list for any new key accessed.
Counting characters (count list): For each word, it counts how many times each letter (from 'a' to 'z') appears.
Hashable key (tuple(count)): The frequency list is converted to a tuple (because lists are unhashable) and used as a dictionary key representing the "signature" of the anagram group.
Grouping words: All words with the same character count tuple (i.e., same letter frequencies) get grouped together in the dictionary.
Return result: Finally, the .values() of the dictionary contain lists of anagrams grouped together.
'''


def anagrams(self, arr):
    ans = defaultdict(list)  # Create a dictionary where each key maps to a list (to hold groups of anagrams)

    # Iterate over each word in the input list
    for string in arr:
        count = [0] * 26  # Initialize a list of 26 zeros to count each letter's frequency (assuming lowercase English letters)

        # Count frequency of each character in the current word
        for char in string:
            count[ord(char) - ord('a')] += 1  # Increment count at index corresponding to character 'c'

        # Use the tuple of counts as a hashable key and append the original word to the corresponding group
        ans[tuple(count)].append(string)

    # Return the grouped anagrams as a list of lists
    return list(ans.values())

# Time complexity: O(n*m)
# Space Complexity: O(n)
# here, n is the size of 'ans'
# and, m is length of 'string'