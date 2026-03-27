import numpy as np

# array of 20 random elements with value between 10 and 50
rand_arr = np.random.randint(10, 50, 20)
print("Original array ", rand_arr)

slice_1 = rand_arr[:10]
print("First 10 elements of the array ", slice_1)

slice_2 = rand_arr[-5:]
print("Last 5 elements of the array: ", slice_2)

slice_3 = rand_arr[5:15]
print("Elements from index 5 to 15 excluded: ", slice_3)

slice_4 = rand_arr[::3]
print("Every third element of the array: ", slice_4)

# assigns a value in the corresponding positions
rand_arr[5:10] = 99
print("The array with values modified from position 5 to 10 excluded: ", rand_arr)

# multidimensional array starting from the original one
rand_reshaped = rand_arr.reshape(5, 4)
print("Multidimensional array: ", rand_reshaped)

slice_1 = rand_reshaped[:, :2]
print("First two columns: ", slice_1)

slice_2 = rand_reshaped[:, -2:]
print("Last two columns: ", slice_2)

slice_3 = rand_reshaped[1:3, 2:3]
print("Second and third row, third column: ", slice_3)

slice_4 = rand_reshaped[::2, ::2]
print("Every two rows and columns: ", slice_4)

rand_reshaped[1:3, 2:3] = 10
print("New multidimensional array: ", rand_reshaped)