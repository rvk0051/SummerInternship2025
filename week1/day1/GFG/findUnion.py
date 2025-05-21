#Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

#The Union of the two arrays can be defined as the set containing distinct elements from both arrays.
# If there are repetitions, then only one element occurrence should be there in the union.

#Note: Elements of a[] and b[] are not necessarily distinct.

class Solution:
    def findUnion(self, a, b):
        # a and b are type cast into set
        # then,their union is taken
        # and it's length is stored in count variable
        count = len(set(a) | set(b))
        return count

#Time Complexity = O(n+m)
#Space Complexity = O(n+m)

if __name__ == "__main__":
    # Take input for first array from user
    arr1=[int(x) for x in input().strip().split()]
    arr2=[int(x) for x in input().strip().split()]
    ob=Solution()
    print(ob.findUnion(arr1, arr2))

#Example:-
#Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3]
#Output: 5
#Explanation: Union set of both the arrays will be 1, 2, 3, 4 and 5. So count is 5.
