from Esercizio_riassuntivo_1 import *

#controlla l'argomento della funzione e se è negativo lo fa diventare positivo
def d_controllo_negativi(funzione):
    def wrapper(*args, **kwargs):
        #richiede che il primo argomento della funzione sia un intero
        if args[0]<0:
            new_args = list(args)
            new_args[0] = abs(new_args[0])
            return funzione(*new_args, **kwargs)
        else: 
            return funzione(*args, **kwargs)
    return wrapper

#DA TESTARE
#eseguire la funzione in base se viene restituita la lista o no
def d_controllo_lista(funzione):
    def wrapper(*args, **kwargs):
        #richiede che il secondo argomento di una funzione sia una collezione
        
        if len(args[1]) !=0:
            if funzione.__name__ == "subList":
                result = funzione(*args, **kwargs)
                return result
        else:
            if funzione.__name__ == "subList_withoutList":
                result = funzione(*args, **kwargs)
                return result
    return wrapper


@d_controllo_negativi
def subList_on_decoration (n, base_list):
    
    #controllo che n sia minore della lunghezza della lista
    if len(base_list)>n:
        #inizializzazione nuova lista
        new_list = []
        end = 0
        
        #verifico che n sia giusto
        print(n)
        
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
    
x = subList_on_decoration(-4, [9, 2, 2, 4, 5, 1, 3, 4])

print(x)
