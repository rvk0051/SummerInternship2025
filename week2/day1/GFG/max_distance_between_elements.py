'''
Maximum Distance between Same Elements

Problem Statement:
Given an array arr[], the task is to find the maximum distance between two occurrences of an element.
If no element has two occurrences, then return 0.

Example:

1.
Input: arr[] = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.

2.
Input: arr[] = [1, 2, 3, 6, 5, 4]
Output: 0
Explanation: No element has two occurrences, so maximum distance = 0.

Solution function is max_distance()
'''


# Python Program to find max distance between two occurrences
# in array using hashing

def max_distance(arr):
    # Stores element to first index mapping
    mp = {}
    res = 0  # res = maximum distance between same elements

    for i in range(len(arr)):

        # If this is the first occurrence of the
        # element, store its index
        if arr[i] not in mp:
            mp[arr[i]] = i

        # Else update max distance
        else:
            res = max(res, i - mp[arr[i]])

    return res

# Time Complexity: O(n)
# Space Complexity: O(n)