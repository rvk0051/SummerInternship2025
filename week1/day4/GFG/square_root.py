'''

Square Root
Given a positive integer n, find the square root of n.
If n is not a perfect square, then return the floor value.
Floor value of any number is the greatest Integer which is less than or equal to that number

Examples:

Input: n = 4
Output: 2
Explanation: Since, 4 is a perfect square, so its square root is 2.

Input: n = 11
Output: 3
Explanation: Since, 11 is not a perfect square, floor of square root of 11 is 3.
'''


# Solution function is floorSqrt:
import math
def floorSqrt(self, n):

    # Using built-in function 'sqrt()'
    res = math.sqrt(n)

    # if the square root of 'n' is an integer, then it's floor value will be that same square root
    # So returning floor value for all the cases
    return int(res)

# Time Complexity - O(log n)
# Space Complexity - O(1)

'''

Better Approach:

Let's say square root of n is sq_root:
sq_root = √n
Squaring both the sides:
sq_root2 = n
Taking log on both the sides:
=> ln(sq_root2) = ln(n)
=> 2*ln(sq_root) = ln(n)
=> ln(sq_root) = 1/2 * ln(n)
To isolate sq_root, exponentiate both sides with base e:
=> sq_root = e1/2 * ln(n)

sq_root is the square root of n:
sq_root = √n = e1/2 * ln(n)

Because of the way computations are done in computers in case of decimals, 
the result from the expression may be slightly less than the actual square root. 
Therefore, we will also consider the next integer after the calculated result as a potential answer.

'''


def floorSqrt(n):
    # Calculating square root using mathematical formula
    res = int(math.exp(0.5 * math.log(n)))

    # If square of res + 1 is less than or equal to n
    # then, it will be our answer
    if (res + 1) ** 2 <= n:
        res += 1

    return res

# Time Complexity: O(1)
# Space Complexity: O(1)