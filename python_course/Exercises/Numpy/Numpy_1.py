import numpy as np

# create the array in the corresponding range of values
arr = np.arange(10, 50)
print (arr)
print("Data type: ", arr.dtype)

# astype converts the value of an array 
# store the converted variable
convert_arr = arr.astype(np.float64)
print("New array type: ", convert_arr.dtype)
print("Converted array: ", convert_arr)

# see the shape of the array
print("Array shape: ", arr.shape)
# convert to multidimensional array
# reshape gives an error if row x column value is not equal to the array length
print("Two-dimensional shape: ", arr.reshape((5,8)))