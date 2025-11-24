import numpy as np

#creo l'array nel corrispettivo intervallo di valori
arr = np.arange(10, 50)
print (arr)
print("Tipo dato: ", arr.dtype)

#astype converte il valore di un array 
#memorizzo la variabile convertita
convert_arr = arr.astype(np.float64)
print("Nuovo tipo array: ", convert_arr.dtype)
print("Array convertito: ", convert_arr)

#vedo la forma dell'array
print("Forma array: ", arr.shape)
#converto in array multidimensionale
#reshape dà errore se il valore riga x il valore colonna non è pari alla lunghezza dell'array
print("Forma bidimensionale: ", arr.reshape((5,8)))