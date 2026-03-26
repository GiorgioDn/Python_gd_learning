import numpy as np

# creation of a one-dimensional array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Using some methods
print("Array shape:", arr.shape)  
print("Array dimensions:", arr.ndim) 
print("Data type:", arr.dtype) 
print("Number of elements:", arr.size)  
print("Sum of elements:", arr.sum()) 
print("Mean of elements:", arr.mean()) 
print("Maximum value:", arr.max())
print("Index of maximum value:", arr.argmax())

# creation of a two-dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

# dtype: data type in the array
arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype)

# shape: array dimensions in each dimension returned as a tuple
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

# arange: creates an array with a sequence of numbers
arr = np.arange(10)
print(arr)

# reshape: changes the shape of the array without changing its data
# reshape throws an error if row value x column value is not equal to the array length
arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)