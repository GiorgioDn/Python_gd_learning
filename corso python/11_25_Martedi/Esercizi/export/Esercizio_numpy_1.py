import numpy as np

arr_lin = np.linspace(0, 1, 12)
print("Array con linspace: ", arr_lin)

arr_reshape = arr_lin.reshape(3, 4)
print("Matrice con reshape: ", arr_reshape)

matrix_rand = np.random.rand(3, 4)
print("Matrice random: ", matrix_rand)

sum_matrix = np.sum(arr_reshape)
print("Somma elementi matrice con reshape: ", sum_matrix)

sum_matrix = np.sum(matrix_rand)
print("Somma elementi matrice random: ", sum_matrix)