import numpy as np

#matrice 6x6 con valori casuali
matrix = np.random.randint(1, 101, (6, 6))
print("Matrice: ", matrix)

sub_matrix = matrix[2:6, 2:6]
print("Sotto matrice: ", sub_matrix)

#inverso righe
invert_matrix = sub_matrix[::-1]
print("Sotto matrice invertita: ", invert_matrix)

#valori diagonali
diagonal_array = invert_matrix.diagonal()
print("Elementi nella diagonale: ", diagonal_array)

#uso del select, popola la matrice in base alla corrispettiva condizione e scelta
condition = [invert_matrix%3 == 0]
chooice = [-1]
select_matrix = np.select(condition, chooice)
print("Select matrix: ", select_matrix)

#uso dello slicing booleano
new_invert = invert_matrix
new_invert[invert_matrix%3 == 0] = -1
print("New invert matrix: ", new_invert)