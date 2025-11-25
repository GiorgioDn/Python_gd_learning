import numpy as np

#genero l'array con elementi random in un certo intervallo
rand_arr = np.random.randint(1, 100, 15)

#calcolo la somma e la media
sum = rand_arr.sum()
mean = rand_arr.mean()

print("L'array generato è: ", rand_arr)
print("La somma dell'array è: ", sum)
print("La media degli array è: ", mean)