import numpy as np

"""
COMPLETE NUMPY BROADCASTING EXAMPLES
----------------------------------------
This file contains a series of practical and commented examples
to show how broadcasting works in NumPy.
"""

print("\n=== 1) Broadcasting with scalar ===")
a = np.array([1, 2, 3])
b = 10
print("Array a:", a)
print("Scalar b:", b)
print("a + b =", a + b)   # Every element of a receives +10


print("\n=== 2) Sum between row vector and column vector ===")
row = np.array([1, 2, 3])        
col = np.array([[10], [20]])     
print("row shape:", row.shape)
print("col shape:", col.shape)
print("row + col =\n", row + col)
# Broadcasting creates a 2x3 matrix


print("\n=== 3) Broadcasting between matrix and row vector ===")
A = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([10, 20, 30])  
print("A shape:", A.shape)
print("v shape:", v.shape)
print("A + v =\n", A + v)
# v is replicated for each row


print("\n=== 4) Broadcasting between matrix and column vector ===")
A = np.array([[1, 2, 3], [4, 5, 6]])
v_col = np.array([[10], [20]])   # shape (2,1)
print("A + v_col =\n", A + v_col)
# v_col is replicated per column


print("\n=== 5) Multiplication matrix x row vector ===")
A = np.arange(12).reshape(3, 4)
v = np.array([1, 2, 3, 4])
print("A:\n", A)
print("v:", v)
print("A * v =\n", A * v)
# v scales the columns


print("\n=== 6) 3D Broadcasting: 2D matrix + 1D vector ===")
M = np.ones((2, 3, 4))    
v = np.array([1, 2, 3, 4]) 
print("M shape:", M.shape)
print("v shape:", v.shape)
print("M + v =\n", M + v)
# v is applied to the last dimension


print("\n=== 7) Broadcasting for normalization ===")
X = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])
mean = X.mean(axis=0)   # mean per column
print("Mean per column:", mean)
print("Normalized X =\n", X - mean)
# The mean vector is automatically subtracted from all rows


print("\n=== 8) Broadcasting for Euclidean distances ===")
points = np.array([[0, 0],
                   [1, 0],
                   [0, 1]])
origin = np.array([0, 0])
print("Distance of points from the origin =", np.sqrt(((points - origin)**2).sum(axis=1)))
# origin shape (2,) is broadcasted onto the (3,2) array


print("\n=== 9) Broadcasting with boolean masks ===")
x = np.arange(10)
mask = np.array([True, False, True, False, True, False, True, False, True, False])
# mask shape (10,) → perfect for x shape (10,)
print("x[mask] =", x[mask])
# Here it is not exactly broadcasting, but it works as vector selection


print("\n=== 10) Broadcasting with manual reshape ===")
a = np.arange(4)       # shape (4,)
b = np.arange(3).reshape(3,1)   # shape (3,1)
print("a:", a)
print("b:\n", b)
print("a + b =\n", a + b)
# Force broadcasting on two compatible dimensions


print("\n=== END EXAMPLES ===\n")