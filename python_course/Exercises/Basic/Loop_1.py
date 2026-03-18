repeat = True

#creo un ciclo while che si ripete finchè l'utente vuole
while repeat:
    #prendo il numero in input
    num = int(input("Digitare un numero positivo: "))
    #controllo che il numero sia positivo
    if num<0:
        print("Il numero non è valido")
    else: 
        #stampo i numeri in ordine decrescente
        for n in range(num, -1, -1):
            print(n)
            
    #chiedo all'utente per l'uscita del while
    ask = input("Si vuole continuare? ")
    if ask.lower() == "no":
        repeat = False