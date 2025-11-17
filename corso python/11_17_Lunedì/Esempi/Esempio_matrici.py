#creo la matrice
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#accedo all'elemento nella posizione corrispondente
elemento = matrice[0][1]
print(elemento, "\n")

#stampo gli elementi singolarmente
for riga in matrice:
    for elemento in riga:
        print(elemento)