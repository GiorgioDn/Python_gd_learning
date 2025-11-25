import numpy as np

#Inversa di una matrice
#creazione di una matrice quadrata
quad = np.array([[1, 2], [3, 4]])

#inversa della matrice
quad_inv = np.linalg.inv(quad)
print("Inversa di quad:\n", quad_inv)

#norma di vettore
#creazione del vettore
vector = np.array([3, 4])

#norma del vettore
norm_vector = np.linalg.norm(vector)
print("Norma di vector:", norm_vector)


#creazzione matrice e vettore
matrix_A = np.array([[3, 1], [1, 2]])
vector_B = np.array([9, 8])

#soluzione del sistema di equazioni Ax = B
#A è una matrice, B è un vettore o matrice
x = np.linalg.solve(matrix_A, vector_B)
print("Soluzione x:", x) 

#Trasformata di fourier
#creazione di un segnale
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

#calcolo della Trasformata di Fourier
fft_sig = np.fft.fft(sig)

#frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasformata di Fourier:", fft_sig)
print("Frequenze associate:", freqs)