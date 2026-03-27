# 4x4 matrix with sequence of random numbers
matrix = np.random.randint(10, 51, 16).reshape(4, 4)
print("Matrix: ", matrix)

# elements in position (0,1)
position = [0, 1]
print(f"Matrix at position {position}: {matrix[position]}")

# elements in position (1,3)
position = [1, 3]
print(f"Matrix at position {position}: {matrix[position]}")

# elements in position (2,2)
position = [2, 2]
print(f"Matrix at position {position}: {matrix[position]}")

# elements in position (3,0)
position = [3, 0]
print(f"Matrix at position {position}: {matrix[position]}")

# print elements in odd positions
odd_indices = np.arange(0, matrix.shape[0], 2)
print(f"Odd rows of the matrix: {matrix[odd_indices]}")

# modify elements by adding 10 
position = [0, 1]
ten_sum = matrix[position] + 10
print(f"Elements in position {position} were added to 10: {ten_sum}")