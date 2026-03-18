import numpy as np

arr = np.array([10, 20, 30, 40, 50])

#utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices])

#utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices])