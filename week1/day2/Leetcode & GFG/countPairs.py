#Count Pairs Whose Sum is Less than Target

#Given a 0-indexed integer array nums of length n and an integer target,
#return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

#Example:
#Input: nums = [-1,1,2,3,1], target = 2
#Output: 3
#Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
#(0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
#(0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target
#(0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
#Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.

#Used Two-Pointer Technique

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        length = len(nums) #Calculating length of given list
        sorted_arr = sorted(nums) #Sorting the array

        left = 0 #Pointing to the leftmost index of list
        right = length-1 ##Pointing to the rightmost index of list

#If length is 1 or 0, then a pair can't exist, that's why returning 0
        if length <= 1:
            return 0

        while left != right:
            if sorted_arr[left] + sorted_arr[right] < target :
                pairs += pairs + (right - left)
# If the condition meets, no. of all the pairs possible with arr[left] is (right - left)
                left = left + 1
# increasing index as all the pairs with arr[left] has been counted.
            elif sorted_arr[left] + sorted_arr[right] >= target:
                right = right - 1
# decreasing index as the element at that index is that greater that no pair is possible with arr[right]
        return pairs


#Time Complexity: O(n log n)
#As sorting took O(n log n) and loop which finds the pair is using O(n) in worst case

#Space Complexity: O(n)
#as a new sorted array is created of size n