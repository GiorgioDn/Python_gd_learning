#dichiarazione del decoratore
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

#inizializzo il decoratore 
@decoratore
def saluta():
    print("Ciao")

#lancio la funzione saluta modificata dal wrapper
saluta()

print()

#decoratore con argomenti
def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print ("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a + b)
    return a + b

#utilizzo lo stesso wrapper una funzione con più parametri
@decoratore_con_argomenti
def sommaMultipla(a, b, c, d):
    print(a + b + c + d)
    return a + b + c + d

print("Il risultato è:", somma(4, 5))

print("Il risultato è:", sommaMultipla(1, 2, 4, 3))

def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiama a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione (*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica (a, b):
    return a*b

moltiplica (3, 5)