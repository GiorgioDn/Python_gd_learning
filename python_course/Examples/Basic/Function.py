#definizione funzione saluta
def saluta(nome):
    print("Ciao,", nome)
    print("Benvenuto nel nostro programma")

#definizione funzione somma
def somma(a, b):
    risultato = a + b
    print("La somma è:", risultato)
    
#eseguo le funzioni dichiarate 
saluta("Alice")
somma(3, 4)

#funzione con return
def quadrato(num):
    return num * num

#memorizzo il risultato restituito dalla funzione in una variabile
risultato = quadrato(2)
print("Il quadrato è:", risultato)