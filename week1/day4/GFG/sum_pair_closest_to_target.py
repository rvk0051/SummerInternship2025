'''
Given an array arr[] and a number target, find a pair of elements (a, b) in arr[],
where a<=b whose sum is closest to target.

Note: Return the pair in sorted order and if there are multiple such pairs
      return the pair with maximum absolute difference.
      If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.

Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3.
             Hence, [2, 7] has maximum absolute difference and closest to target.

'''

# Solution function is named as sumClosest

def sumClosest(self, arr, target):

    # function to return the pair with sum closest to target
    # using Two Pointer Technique

    arr.sort()  # sorting the array
    res = []  # 'res' is the list for storing resultant pair

    length = len(arr)

    # if there is one element in arr, no pair can exist
    if length <= 1: return res

    # if length = 2, then only one pair exists, that's why that pair will be the result
    if length == 2:
        return [arr[0], arr[1]]

    left = 0
    right = length - 1

    # we need to find the smallest difference between target and sum of the elements in pair
    # so we need to initialize 'minDiff' with a value which is guaranteed
    # to be larger than any possible difference we might calculate.
    minDiff = float('inf')

    while left < right:

        sum = arr[left] + arr[right]

        # Check if this pair is closer than the closest pair so far
        if abs(target - sum) < minDiff:
            res = [arr[left], arr[right]]
            minDiff = abs(target - sum)

        # If this pair has sum = target, break the while loop
        if target == sum:
            break
        # If this pair has more sum, move to smaller values
        elif target < sum:
            right -= 1

        # If this pair has less sum, move to greater values
        elif target > sum:
            left += 1

    return res