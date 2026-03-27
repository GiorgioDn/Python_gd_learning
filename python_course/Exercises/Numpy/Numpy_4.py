import numpy as np

# create arrays on two separate arrays and then concatenate them
fixed_array = np.arange(0,50)
random_array = np.random.randint(49, 101, 50)
array = np.concatenate((fixed_array, random_array))
print(f"Array: {array} \n Dtype: {array.dtype}\n Shape: {array.shape}")

# dtype modification
new_dtype = np.array(array, dtype="float64")
print(f"Array: {new_dtype} \n Dtype: {new_dtype.dtype}\n Shape: {new_dtype.shape}")

# slicing first 10 elements
first_ten = array[:10]
print("First 10 elements: ", first_ten)

# slicing last 7 elements
last_seven = array[-7:]
print("Last 7 elements: ", last_seven)

# slicing index 5 to 20 excluded
slice_5_to_20 = array[5:20]
print("From index 5 to 20 excluded: ", slice_5_to_20)

# every fourth element of the array
every_four = array[::4]
print("Every fourth element of the array: ", every_four)

# modify elements to 999
new_arr = np.array(array)
new_arr[10:15] = 999
print("Position value 10 to 15 excluded to 999: ", new_arr)

# fancy indexing
index = [0, 3, 7, 12, 25, 33, 48]
print("Array with fancy indexing: ", array[index])

# even elements with a boolean mask
even_mask = np.array(array)
print("Even elements: ", even_mask[even_mask%2==0])

# elements greater than the array mean
mean = np.mean(array)
print(f"Elements greater than {mean}: {array[array>mean]}")