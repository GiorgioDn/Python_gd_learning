import numpy as np

arr_lin = np.linspace(0, 1, 12)
print("Array with linspace: ", arr_lin)

arr_reshape = arr_lin.reshape(3, 4)
print("Matrix with reshape: ", arr_reshape)

matrix_rand = np.random.rand(3, 4)
print("Random matrix: ", matrix_rand)

sum_matrix = np.sum(arr_reshape)
print("Sum of elements of matrix with reshape: ", sum_matrix)

sum_matrix = np.sum(matrix_rand)
print("Sum of elements of random matrix: ", sum_matrix)

mat_add = np.add(arr_reshape, matrix_rand)
print("Sum matrix: ", mat_add)