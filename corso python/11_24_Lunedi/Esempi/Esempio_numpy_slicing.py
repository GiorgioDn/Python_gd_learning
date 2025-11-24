import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#slicing di base
print(arr[2:7])

#slicing con passo
print(arr[1:8:2])  # Output: [1 3 5 7]

#omettere start e stop
print(arr[:5])
print(arr[5:])

#indici negativi
print(arr[-5:])
print(arr[:-5])