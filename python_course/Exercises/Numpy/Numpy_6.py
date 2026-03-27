import numpy as np

# generate array with random elements in a certain range
rand_arr = np.random.randint(1, 100, 15)

# calculate sum and mean
total_sum = rand_arr.sum()
mean = rand_arr.mean()

print("The generated array is: ", rand_arr)
print("The sum of the array is: ", total_sum)
print("The mean of the array is: ", mean)