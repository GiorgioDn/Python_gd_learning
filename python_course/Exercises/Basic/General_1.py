""" 
    Creare una funzione che prende un intero positivo per generare una sottolista dei primi n elementi di una lista definita dall'utente, inoltre la funzione deve far scegliere se restituire la sottolista, eliminare i duplicati o verificare le eventuali differenze tra la lista e la sottolista.
"""
from random import randint

#funzione per eseguire le funzionalità dell'esercizio
def subList (n, base_list):
    
    #controllo che n sia minore della lunghezza della lista
    if len(base_list)>n:
        #inizializzazione nuova lista
        new_list = []
        end = 0
        
        #riempio la nuova lista
        while end < n:
            new_list.append(base_list[end])
            end +=1
        
        #scelta dell'operazione
        chooice = int(input("Scegliere una delle seguenti operazioni: \n 1. Restituire la sottolista \n 2. Eliminare i duplicati della sottolista\n 3. Verificare gli elementi diversi della sottolista \n"))
        
        match chooice:
            case 1:
                return new_list
            case 2:
                #conversione per eliminare i duplicati
                list_without_double = set(new_list)
                return list_without_double
            case 3:
                #faccio la comparazione delle due liste
                set_new = set(new_list)
                set_ori = set(base_list)
                return set_ori.difference(set_new)
            case _:
                return False
    else:
        return False

#in caso non si inserisca una lista in input      
def subList_withoutList (n):
    
    #inizializzazione nuova lista con numeri casuali
    
    new_list = []
    end = 0
    base_list = []
    
    #creo la lista iniziale con valori random
    for num in range(n+1):
        base_list.append(randint(0, n*2))
    
    #riempio la nuova lista
    while end < n:
        new_list.append(base_list[end])
        end +=1
    
    #scelta dell'operazione
    chooice = int(input("Scegliere una delle seguenti operazioni: \n 1. Restituire la sottolista \n 2. Eliminare i duplicati della sottolista\n 3. Verificare gli elementi diversi della sottolista \n"))
    
    match chooice:
        case 1:
            return new_list
        case 2:
            #conversione per eliminare i duplicati
            list_without_double = set(new_list)
            return list_without_double
        case 3:
            #faccio la comparazione delle due liste
            set_new = set(new_list)
            set_ori = set(base_list)
            return set_ori.difference(set_new)
        case _:
            return False

#fa eseguire la funzione in automatico quando viene importata 
#x = subList(4, [9, 2, 2, 4, 5, 1, 3, 4])

#print(x)