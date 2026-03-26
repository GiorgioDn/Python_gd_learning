# create the matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# access the element at the corresponding position
element = matrix[0][1]
print(element, "\n")

# print the elements individually
for row in matrix:
    for element in row:
        print(element)