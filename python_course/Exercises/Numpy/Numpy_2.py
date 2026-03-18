import numpy as np

#array di 20 elementi random di valore compreso tra 10 e 50
rand_arr = np.random.randint(10, 50, 20)
print("Array originale ", rand_arr)

slice_1 = rand_arr[:10]
print("Primi 10 elementi dell'array ", slice_1)

slice_2 = rand_arr[-5:]
print("Ultimi 5 elementi dell'array: ", slice_2)

slice_3 = rand_arr[5:15]
print("Elementi dall'indice 5 al 15 escluso: ", slice_3)

slice_4 = rand_arr[::3]
print("Ogni terzo elemento dell'array: ", slice_4)

#assegna un valore nelle posizioni corrispondenti
rand_arr[5:10] = 99
print("L'array con i valori modificati dalla posizione 5 a 10 escluso: ", rand_arr)

#array multidimensionale a partire da quella originale
rand_reshaped = rand_arr.reshape(5, 4)
print("Array multidimensionale: ", rand_reshaped)

slice_1 = rand_reshaped[:, :2]
print("Primi due colonne: ", slice_1)

slice_2 = rand_reshaped[:, -2:]
print("Ultime due colonne: ", slice_2)

slice_3 = rand_reshaped[1:3, 2:3]
print("Seconda e terza riga, terza colonna: ", slice_3)

slice_4 = rand_reshaped[::2, ::2]
print("Ogni due righe e colonne: ", slice_4)

rand_reshaped[1:3, 2:3] = 10
print("Nuova array multidimensionale: ", rand_reshaped)