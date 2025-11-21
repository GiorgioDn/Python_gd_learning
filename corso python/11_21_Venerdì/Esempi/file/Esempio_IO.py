#apre il file in lettura
file = open("corso python/11_21_Venerdì/Esempi/file/test.txt", "r") 

#legge l'intero contenuto del file
contenuto = file.read()
print(contenuto)

#legge una riga del file 
riga = file.readline()
print(riga)

#apre il file in scrittura sovrascrivendone il contenuto
file = open("corso python/11_21_Venerdì/Esempi/file/test.txt", "w") 

file.write("Ciaoooo, forse")
#chiusura del file
file.close()

#con with open il file viene chiuso automaticamente alla fine
with open ("corso python/11_21_Venerdì/Esempi/file/test.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)