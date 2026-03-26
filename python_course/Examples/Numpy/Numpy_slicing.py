import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# basic slicing
print(arr[2:7])

# slicing with step
print(arr[1:8:2])  # Output: [1 3 5 7]

# omitting start and stop
print(arr[:5])
print(arr[5:])

# negative indices
print(arr[-5:])
print(arr[:-5])