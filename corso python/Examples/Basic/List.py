#Dati liste
numeri = [1, 2, 3, 4, 5]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, 2, "Bob", False]

#Si accede agli elementi di una lista con l'indice partendo da 0
print(numeri[0])
print(nomi[1])
print(misto[3])

#si può modificare un elemento tramite l'indice
numeri[2] = 20
print(numeri)

#alcuni metodi sono
#len per la lunghezza 
print(len(numeri))
#append per aggiungere un elemento a fine lista
numeri.append(6)
print(numeri)
#insert per inserire un elemento in una posizione specifica
numeri.insert(1, 10)
print(numeri)
#remove per rimuovere un elemento
numeri.remove(4)
print(numeri)
#sort per organizzare la lista
numeri.sort()
print(numeri)
#pop toglie l'ultimo elemento di una lista
numeri.pop()
print(numeri)