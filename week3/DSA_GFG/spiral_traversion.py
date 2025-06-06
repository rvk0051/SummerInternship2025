# Spiral traverse a matrix
'''
Problem Statement:-
You are given a rectangular matrix mat[][] of size n x m, and your task is to
return an array while traversing the matrix in spiral form.

Example:-
Input:
n = 4, m = 4
mat[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15, 16}}
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Solution function is 'spirallyTraverse'
'''

# Python program to perform spiral order
# traversal of a matrix

def spirallyTraverse(mat):
    no_of_rows, no_of_columns = len(mat), len(mat[0])

    result = []

    # Initialize boundaries
    top, bottom, left, right = 0, no_of_rows - 1, 0, no_of_columns - 1

    # Iterate until all elements are printed
    while top <= bottom and left <= right:

        # Print top row from left to right
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1

        # Print right column from top to bottom
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1

        # Print bottom row from right to left (if exists)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1

        # Print left column from bottom to top (if exists)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1

    return result

# Time Complexity: O(m*n), where m and n are the number of rows and columns of the given matrix respectively.
# Auxiliary Space: O(1)
