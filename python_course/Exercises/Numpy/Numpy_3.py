import numpy as np

# 6x6 matrix with random values
matrix = np.random.randint(1, 101, (6, 6))
print("Matrix: ", matrix)

sub_matrix = matrix[2:6, 2:6]
print("Sub-matrix: ", sub_matrix)

# reverse rows
reversed_matrix = sub_matrix[::-1]
print("Reversed sub-matrix: ", reversed_matrix)

# diagonal values
diagonal_array = reversed_matrix.diagonal()
print("Elements in the diagonal: ", diagonal_array)

# use of select, populates the matrix based on the corresponding condition and choice
condition = [reversed_matrix%3 == 0]
choice = [-1]
select_matrix = np.select(condition, choice)
print("Select matrix: ", select_matrix)

# use of boolean slicing
new_reversed = reversed_matrix
new_reversed[reversed_matrix%3 == 0] = -1
print("New reversed matrix: ", new_reversed)