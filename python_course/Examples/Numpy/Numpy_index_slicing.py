import numpy as np

# Indexing and slicing
arr = np.array([1, 2, 3, 4, 5])

print("Indexing\n")
# indexing
print(arr[0], "\n")

print("Slicing\n")
# slicing
print(arr[1:3], "\n")

print("Boolean indexing\n")
# boolean indexing
print(arr[arr > 2], "\n")


arr_2d = np.array([[1, 2, 3, 4],

                   [5, 6, 7, 8],

                   [9, 10, 11, 12]])

print("Slicing on rows")
# slicing on rows
print(arr_2d[1:3], "\n")

print("Slicing on columns")
# slicing on columns
print(arr_2d[:, 1:3], "\n")

print("Slicing on rows and columns")
# mixed slicing
print(arr_2d[1:, 1:3], "\n")