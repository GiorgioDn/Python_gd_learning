#tipi di variabili interi
x = 1
y = -5

print(x, y)

#tipi di variabili float (usa il . e non la ,)
x = 3.14
y = -5.46

print(x, y)

#tipi di variabili stringhe
x = "more"
y = "metri"

print(x, y)

#indice del char di una stringa 
print("Char m della stringa x: ", x[0])
print("Char r della stringa y: ", y[3])

#concatenazione stringhe
conc = x + " 3.3 " + y 

print(conc)

#metodi stringhe
#len = lunghezza stringa
print(len(x))

#upper = converte stringa in maiuscolo
print(x.upper())

#lower = converte stringa in minuscolo
print(x.lower())

#split = divide in una lista di sottostringhe
print(conc.split())

#in base anche ad un delimitatore
concDel = conc + ", " + x
print(concDel.split(','))

#replace = sostituisce parte di una stringa con un'altra
print(conc.replace('more', 'distanza'))

#tipo char
char = "A"
print(char)

#tipi di variabili booleane True o False
x = True
y = False 

print(x, y)

#I valori booleani True o False si possono usare con operatori logici 
x = 5
y = 10
z = 7

#and restituisce true con entrambe le condizione vere
print("Il valore booleano di: x < y and z < y è:", x < y and z < y)

#or restituisce true se almeno una delle condizioni è vera
print("Il valore booleano di: x < y or x > z è:", x < y or x > z)

#not restituisce il valore booleano opposto di ciò che segue
print("Il valore booleano di: not(x < y) è:", not(x < y))

#operatori di confronto, restituiscono un valore booleano
#== uguale a
print("Il valore booleano di: x == y è:", x == y)

#!= diverso da 
print("Il valore booleano di: x != y è:", x != y)

# < minore di 
print("Il valore booleano di: x < y è:", x < y)

#> maggiore di 
print("Il valore booleano di: x > y è:", x > y)

#<= minore o uguale a 
print("Il valore booleano di: x <= y è:", x <= y)

#>= maggiore o uguale a
print("Il valore booleano di: x >= y è:", x >= y)