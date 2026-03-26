import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# using an array of indices
indices = np.array([1, 3])
print(arr[indices])

# using a list of indices
indices = [0, 2, 4]
print(arr[indices])