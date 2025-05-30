# Count number of times graph cuts x-axis
'''
Given an integer array arr[] of size n, the task is to find the number of times the graph crosses the X-axis,
where a positive number in arr[] means going above its current position by that value and
a negative number means going down by that value.
Initially, the current position is at the origin.


Example 1:

Input: arr[] = [2, 5, -9, 4]
Output: 2
Explanation: Graph touches the X-axis two times through index 1 to 2, and through index 2 to 3.


Example 2:

Input: arr[] = [1, 3, 5]
Output: 0
Explanation: Graph has not touched the X-axis any time.

Solution function is 'touchedXaxis()'.

Approach:-

The idea is to iterate through the array and observe the previous and current levels of 'sum' after each iteration .
The current level at index i can be calculated by taking the prefix sum arr[0...i].
As we update the current level by adding the value at each index to the previous level.

We increment the crossing count whenever one of these conditions is met:
If the previous level is negative and the current level is zero or positive.
If the previous level is positive and the current level is zero or negative.
'''

# Solution functionL- touchedXaxis()
# 'touchedXaxis() returns the no. of times the graph has cut x-axis
def touchedXaxis(self, arr):

    count = 0

    # iterating through the array
    for i in range(len(arr)):

        # 'prev_sum' stores the previous level of sum
        prev_sum = sum
        sum = arr[i] + sum

        # comparing prev_sum and sum
        if (prev_sum < 0 and sum >= 0) or (prev_sum > 0 and sum <= 0):
            # if any of these 2 conditions meet, means that the graph cuts the x-axis
            # that's why increasing the counter.
            count += 1

    # returning 'count'
    return count

# Time Complexity:- O(n)  ## due to iterating 'arr'
# Space Complexity:- O(1)