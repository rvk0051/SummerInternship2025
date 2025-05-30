# Rotate matrix by 180 degree
'''
Given a square matrix, the task is to turn it by 180 degrees.
Note that when we rotate a matrix by 180 degree, clockwise and anticlockwise both give same results.
'''

# Examples:-
'''
1.
Input: 
mat[][] = [[1, 2, 3]
[4, 5, 6]
[7, 8, 9]]

Output: 
[9, 8, 7]
[6, 5, 4]
[3, 2, 1]


2.
Input: 
mat[][] = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2],
[3, 4, 5, 6]]

Output: 
[[6, 5, 4, 3],
[2, 1, 0, 9],
[8, 7, 6, 5],
[4, 3, 2, 1]]
'''

# Solution function is 'rotateMatrix()'

def rotateMatrix(mat):
    # Function to rotate the matrix by 180 degrees

    size = len(mat)

    # Swap elements from start and end to
    # rotate by 180 degrees
    for i in range(size // 2):
        for j in range(size):
            mat[i][j], mat[size - i - 1][size - j - 1] = mat[size - i - 1][size - j - 1], mat[i][j]

    # Handle the middle row if the matrix
    # has odd dimensions
    if size % 2 != 0:
        mid = size // 2
        for j in range(size // 2):
            mat[mid][j], mat[mid][size - j - 1] = mat[mid][size - j - 1], mat[mid][j]
            # swapping elements of middle row.


# Time complexity: O(n^2)
# Space complexity: O(1)