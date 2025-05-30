# Generate a matrix with each row and column of given sum

'''
Find Matrix With Given Row and Column Sums
Given two arrays rowSum[] and colSum[] of size n and m respectively,
the task is to construct a matrix of dimensions n × m such that the sum of matrix elements in
every ith row is rowSum[i] and the sum of matrix elements in every jth column is colSum[j].

Note: The resultant matrix can have only non-negative integers.

Example:-

Input: rowSum[] = [5, 7, 10], colSum[] = [8, 6, 8]

Output: [[0, 5, 0],
[6, 1, 0],
[2, 0, 8]]

Explanation:
Row 1 has sum equal to 5 and column 1 has sum equal to 8.
Row 2 has sum equal to 7 and column 2 has sum equal to 6.
Row 3 has sum equal to 10 and column 3 has sum equal to 8.
'''

# Solution function is 'generateMatrix'
def generateMatrix(rowSum, colSum):

    row_length = len(rowSum)  # size of the array 'rowSum'
    col_length = len(colSum)  # size of the array 'colSum'

    # initialize the resultant matrix with zeros
    resultant_matrix = [[0] * col_length for _ in range(row_length)]

    # initializing indices
    i = 0
    j = 0


    while i < row_length and j < col_length:

        # set the value of the 'resultant_matrix[i][j]' values to the minimum of rowSum[i] and colSum[j]
        resultant_matrix[i][j] = min(rowSum[i], colSum[j])

        # we subtract the value of 'resultant_matrix[i][j]' from rowSum[i] and colSum[j],
        # so that rowSum[i] and colSum[j] become their remaining sums.
        rowSum[i] -= resultant_matrix[i][j]
        colSum[j] -= resultant_matrix[i][j]

        # after subtraction either rowSum[i] or colSum[j] becomes zero.

        # if rowSum[i] becomes zero, it means that the current row is filled, that's why incrementing the row.
        if rowSum[i] == 0:
            i += 1

        # if colSum[j] becomes zero, it means that the current column is filled, that's why incrementing the column.
        if colSum[j] == 0:
            j += 1

    return resultant_matrix

'''
Time Complexity: O(n+m)
as we iterate through rowSum and colSum arrays.

Space Complexity: O(n*m)

'''