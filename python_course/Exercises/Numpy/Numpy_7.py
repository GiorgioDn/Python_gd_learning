import numpy as np

# 5x5 matrix with number sequence
matrix = np.arange(1,26).reshape(5, 5)
print("Matrix: ", matrix)

# second column of the matrix
second_col = matrix[: , 1:2]
print("Second column of the matrix: ", second_col)

# third row of the matrix
third_row = matrix[2:3]
print("Third row of the matrix: ", third_row)

# sum of the main diagonal
sum_diag = np.diag(matrix).sum()
print("The sum of the main diagonal is: ", sum_diag)
