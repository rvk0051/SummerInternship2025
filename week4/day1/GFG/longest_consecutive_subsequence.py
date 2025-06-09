# Longest Consecutive Subsequence
'''
Problem Statement:-
Given an array arr[] of non-negative integers.
Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers,
the consecutive numbers can be in any order.

Example1:
Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.

Example2:
Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

Solution function is 'longestConsecutive
'''

# Approach1:
'''
The idea is to sort the array and find the longest subarray with consecutive elements. I
nitialize the consecutive count with 1 and start iterating over the sorted array from the second element. 
For each element arr[i], we can have three cases:
* arr[i] = arr[i - 1], then the ith element is simply a duplicate element so skip it.
* arr[i] = arr[i - 1] + 1, then increase the consecutive count and update result if consecutive count is greater than result.
* arr[i] > arr[i - 1], then reset the consecutive count to 1.
After iterating over all the elements, return the count of longest subsequence.
'''
def longestConsecutive(self, arr):

    #sorting the array so that the consecutive numbers are in order
    arr.sort()
    size = len(arr)

    # if the array has no element, then there are not even any number.
    if size == 0: return 0

    # initializing max_count which keep records of the longest consecutive subsequence.
    max_count = 1

    # initializing the count of consecutive numbers  as 1, as if there is a single number in the array, it is a consecutive number.
    count = 1

    # iterating through array
    for i in range(1, size):

        # if the consecutive numbers are same, then we will skip the number
        if arr[i] == arr[i - 1]:
            continue

        # if the numbers are consecutive then we will increment the count of consecutive numbers.
        elif arr[i] == arr[i - 1] + 1:
            count += 1

        else:
            # reinitializing the count as 1.
            count = 1

        # updating the max_count.
        max_count = max(max_count, count)

    return max_count
# Time Complexity: O(n log n), where n is the size of the array.
# Auxiliary Space: O(1)