import numpy as np

#matrice 4x4 con sequenza di numeri casuali
matrix = np.random.randint(10, 51, 16).reshape(4, 4)
print("Matrice: ", matrix)

#elementi in posizione (0,1)
position = [0, 1]
print(f"Matrice in posizione {position}: {matrix[position]}")

#elementi in posizione (1,3)
position = [1, 3]
print(f"Matrice in posizione {position}: {matrix[position]}")

#elementi in posizione (2,2)
position = [2, 2]
print(f"Matrice in posizione {position}: {matrix[position]}")

#elementi in posizione (3,0)
position = [3, 0]
print(f"Matrice in posizione {position}: {matrix[position]}")

#stampare elementi in posizioni dispari
indici_dispari = np.arange(0, matrix.shape[0], 2)
print(f"Righe dispari della matrice: {matrix[indici_dispari]}")

#modificare gli elementi aggiungendo 10 
position = [0, 1]
ten_sum = matrix[position] + 10
print(f"Gli elementi in posizione {position} sono stati sommati a 10: {ten_sum}")