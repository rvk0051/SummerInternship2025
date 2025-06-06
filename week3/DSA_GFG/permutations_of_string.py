# Permutations of a String
'''
Problem Statement:-
Given a string s, which may contain duplicate characters, your task is to generate and
return an array of all unique permutations of the string. You can return your answer in any order.

Example1:-
Input: s = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
Explanation: Given string ABC has 6 unique permutations.

Example2:-
Input: s = "AAA"
Output: ["AAA"]
Explanation: No other unique permutations can be formed as all the characters are same.

Solution function is 'findPermutation'
'''

# 'genPermutations' is recursively called by itself and is called by 'findPermutation'
def genPermutations(length, current, count_occurrences, result):
    # Recursive function to generate permutations
    
    # Base case: If the current permutation length equals 
    # the input string length, add it to the result
    if len(current) == length:
        result.append(current)
        return

    # Iterate through each character in the frequency map
    for char, count in count_occurrences.items():
        # Skip characters with a count of 0
        if count == 0:
            continue

        # Include the character in the current permutation
        count_occurrences[char] -= 1

        # Recur to build the next character in the permutation
        genPermutations(length, current + char, count_occurrences, result)

        # Backtrack: Restore the count
        count_occurrences[char] += 1


# Function to find all unique permutations of the input string
def findPermutation(s):
    # List to store the result
    result = []

    # Frequency map to count occurrences of each character
    count_occurrences = {}

    # Populate the frequency map with the characters of the input string
    for char in s:
        count_occurrences[char] = count_occurrences.get(char, 0) + 1

    # Generate permutations
    genPermutations(len(s), "", count_occurrences, result)
    return result

'''
Time Complexity: O(n*n!), In worst case all characters were unique, so it take time equal to generating all permutations.
Auxiliary Space: O(n), used by temporary string and hash map.
'''