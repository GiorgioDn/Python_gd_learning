import numpy as np

#matrice 5x5 con sequenza di numeri
matrix = np.arange(1,26).reshape(5, 5)
print("Matrice: ", matrix)

#seconda colonna della matrice
second_col = matrix[: , 1:2]
print("Seconda colonna della matrice: ", second_col)

#terza riga della matrice
third_row = matrix[2:3]
print("Terza riga della matrice: ", third_row)

#somma della diagonale principale
sum_diag = np.diag(matrix).sum()
print("La somma della diagonale principale è: ", sum_diag)
