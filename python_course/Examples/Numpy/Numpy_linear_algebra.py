import numpy as np

# Matrix Inverse
# creation of a square matrix
quad = np.array([[1, 2], [3, 4]])

# inverse of the matrix
quad_inv = np.linalg.inv(quad)
print("Inverse of quad:\n", quad_inv)

# vector norm
# creation of the vector
vector = np.array([3, 4])

# norm of the vector
norm_vector = np.linalg.norm(vector)
print("Norm of vector:", norm_vector)


# creation of matrix and vector
matrix_A = np.array([[3, 1], [1, 2]])
vector_B = np.array([9, 8])

# solution to the system of equations Ax = B
# A is a matrix, B is a vector or matrix
x = np.linalg.solve(matrix_A, vector_B)
print("Solution x:", x) 

# Fourier Transform
# creation of a signal
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# calculation of the Fourier Transform
fft_sig = np.fft.fft(sig)

# associated frequencies
freqs = np.fft.fftfreq(len(fft_sig))

print("Fourier Transform:", fft_sig)
print("Associated frequencies:", freqs)