# Nested List

# A nested list is a list within another list, which is useful for representing matrices or tables.
# We can access nested elements by chaining indexes.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[1][2]) # Output: 6

# Accessing first row
print(matrix[0])  # Output: [1, 2, 3]

# Accessing first column
column_0 = [row[0] for row in matrix]
print(column_0) # Output: [1, 4, 7]
