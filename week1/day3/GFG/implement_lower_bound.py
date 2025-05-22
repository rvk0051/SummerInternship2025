# Implement Lower Bound
# Given a sorted array arr[] and a number target, the task is to find the lower bound of the target in this given array.
# The lower bound of a number is defined as the smallest index in the sorted array
# where the element is greater than or equal to the given number.

# Note: If all the elements in the given array are smaller than the target,
# the lower bound will be the length of the array.

# Example:
# Input:  arr[] = [2, 3, 7, 10, 11, 11, 25], target = 9
# Output: 3
# Explanation: 3 is the smallest index in arr[] where element (arr[3] = 10) is greater than or equal to 9.

# Solution:-
# lowerBound function will be called
# Using binary search

def lowerBound(self, arr, target):
    # code here
    size = len(arr)

    result = size
    # if we don't get any index which have element >= target, then we need to return size of the array.

    low = 0
    high = size - 1

    while low <= high:

        mid = low + (high - low) // 2
        # if the mid value is greater or equal to target,
        # the result value gets updated and
        # search in left half, i.e. [lo...mid-1]

        if arr[mid] >= target:
            result = mid
            high = mid - 1
        # If arr[mid] < target, then lower bound
        # cannot lie in the range [lo...mid] so
        # search in right half, i.e. [mid+1...hi]

        else:
            low = mid + 1

    return result

# Time Complexity: O(log n)
# Space Complexity: O(1)