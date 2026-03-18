#importo tutte le funzioni presenti nel file Fibonacci.py
from .Import.Fibonacci import *
        
while True:
    #chiedo il numero della sequenza
    num_fibonacci = int(input("Digitare un numero intero positivo per la sequenza di fibonacci: "))
    #inizializzo la lista con i risultati
    lista_res = []
    #risultato della versione con le successioni
    result = fibonacci_succ(num_fibonacci, lista_res)
    print(result)
    
    #risultato ricorsiva con solo il risultato restituito al num_fibonacci
    result_ric = fibonacci_ricorsiva(num_fibonacci)
    print(result_ric)
    
    chooice = input("Si desidera continuare ad inserire numeri? ")
    
    if chooice.lower() == "no":
        break
