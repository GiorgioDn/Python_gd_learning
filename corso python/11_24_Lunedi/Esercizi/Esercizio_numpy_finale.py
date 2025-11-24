import numpy as np

#creo gli array su due array separati ed infine li concateno
array_fix = np.arange(0,50)
array_ran = np.random.randint(49, 101, 50)
array = np.concatenate((array_fix, array_ran))
print(f"Array: {array} \n Dtype: {array.dtype}\n Shape: {array.shape}")

#modifica del dtype
new_dtype = np.array(array, dtype="float64")
print(f"Array: {new_dtype} \n Dtype: {new_dtype.dtype}\n Shape: {new_dtype.shape}")

#slicing primi 10 elementi
first_ten = array[:10]
print("Primi 10 elementi: ", first_ten)

#slicing ultimi 7 elementi
last_seven = array[-7:]
print("Ultimi 7 elementi: ", last_seven)

#slicing indice 5 a 20 escluso
five_to_twelve = array[5:20]
print("Dall'indice 5 al 20 escluso: ", five_to_twelve)

#ogni quarto elemento dell'array
every_four = array[::4]
print("Ogni quarto elemento dell'array: ", every_four)

#modifica elementi a 999
new_arr = np.array(array)
new_arr[10:15] = 999
print("Valore posizione 10 a 15 esclusa a 999: ", new_arr)

#fancy index
index = [0, 3, 7, 12, 25, 33, 48]
print("Array con fancy index: ", array[index])

#elementi pari con una maschera booleana
bool_arr = np.array(array)
print("Elementi pari: ", bool_arr[bool_arr%2==0])

#elementi maggiori della media dell'array
mean = np.mean(array)
print(f"Elementi maggiori di {mean}: {array[array>mean]}")