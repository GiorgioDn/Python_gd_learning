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