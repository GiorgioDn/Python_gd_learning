#definisco la funzione fibonacci ricorsiva che restituise solo l'ultimo elemento
def fibonacci_ricorsiva(n):

    #ritorno come valore -1 in caso di errore per eventuali
    if n < 0:
        return -1
    elif n< 2:
        return n
    else:
        return (fibonacci_ricorsiva(n-1) + fibonacci_ricorsiva(n-2))

#definisco la funzione fibonacci che ritorna l'elenco degli elementi durante ogni iterazione
def fibonacci_succ(n, lista_res):
    
    a = 0
    b = 1
    count = 1

    while count <= n +1:
        lista_res.append(a)
        count += 1
        successivo = a + b
        a = b
        b = successivo
        
    return lista_res