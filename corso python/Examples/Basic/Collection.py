#creazione di tuple
punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

#stampa degli elementi
print(punto[0])
print(punto[1])

#packing tupla
punto = 1, 4
#unpacking tupla
x, y= punto
#stampa variabili
print(x, y)

#creazione insiemi
#conversione lista a insieme
set1 = set([1, 2, 3, 4, 5])
#creazione set
set2 = {5, 6, 7, 8, 9}
set3 = {1, 2, 3, 3, 4, 4, 5}
#non stampa i duplicati
print(set3)

#operazione di unione: restituisce i valori di entrambi gli insieme
set4 = set1.union(set2)
print(set4)
#operazione di intersezione: restituisce i valori uguali degli insiemi
set4 = set1.intersection(set2)
print(set4)
#operazione di differenza: restituisce i valori non presenti nell'altro insieme
set4 = set1.difference(set2)
print(set4)
#operazione di differenza simmetrica: restituisce i valori diversi degli insiemi
set4 = set1.symmetric_difference(set2)
print(set4)

#add: aggiunge un elemento
colori = {"rosso", "blu"}
colori.add("verde")
print(colori)
#remove: rimuove l'elemento, genera errore se l'elemento non è presente 
colori.remove("verde")
print(colori)
#discard: come remove, ma senza errore
colori.remove("rosso")
print(colori)
#len: restituisce la lunghezza dell'insieme
print(len(set2))
#copy: copia due insiemi
set4 = set1.copy()
print(set4)