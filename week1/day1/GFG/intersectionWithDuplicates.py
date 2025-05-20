#question:-
#Given two integer arrays a[] and b[], you have to find the intersection of the two arrays.
#Intersection of two arrays is said to be elements that are common in both arrays.
#The intersection should not have duplicate elements and the result should contain items in any order.

class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        resultant_list = []
        # made an empty list to store the result

        set1 = set(a)  # type cast a and b into sets set1 and set2 respectively
        set2 = set(b)

        # Searching if item in set1 is present in set2 or not
        # if it's there, adding it to the resultant_list
        for item in set1:
            if item in set2:
                resultant_list.append(item)

        # Returning resultant list
        return resultant_list

if __name__ == "__main__":
    # Take input for first array from user
    arr1 = [int(x) for x in input().strip().split()]
    arr2 = [int(x) for x in input().strip().split()]
    ob = Solution()
    print(ob.intersectionWithDuplicates(arr1, arr2))

#Example:-
#Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
#Output: [1, 3]
#Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.