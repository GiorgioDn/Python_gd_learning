import numpy as np

#creazione di un array unidimensionale
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape)  
print("Dimensioni dell'array:", arr.ndim) 
print("Tipo di dati:", arr.dtype) 
print("Numero di elementi:", arr.size)  
print("Somma degli elementi:", arr.sum()) 
print("Media degli elementi:", arr.mean()) 
print("Valore massimo:", arr.max())
print("Indice del valore massimo:", arr.argmax())

#creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

#dtype: tipo di dati nell'array
arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype)

#shape: dimensioni dell'array in ciascuna dimensione restituite come tupla
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

#arange: crea un array con una sequenza di numeri
arr = np.arange(10)
print(arr)

#reshape: cambia la forma dell'array senza cambiarne i dati
#reshape dà errore se il valore riga x il valore colonna non è pari alla lunghezza dell'array
arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)