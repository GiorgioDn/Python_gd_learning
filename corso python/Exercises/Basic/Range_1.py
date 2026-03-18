#interrompo il while con il break
while True:
    #scelta dell'input
    chooice = int(input("Scegliere 1 per inserire una stringa, 2 per un numero: "))
    
    if chooice == 1:
        chooice = input("Inserire una stringa: ")
        #prendo la lunghezza della stringa
        pair = len(chooice)
        #vedo se le lettere della stringa sono pari o dispari
        if pair%2 == 0:
            print("La stringa contiene un numero pari di lettere: ", pair)
        else:
            print("La stringa contiene un numero dispari di lettere: ", pair)
    elif chooice == 2:
        chooice = int(input("Inserire un numero: "))
        #vedo se le lettere della stringa sono pari o dispari
        if chooice%2 == 0:
            print("Il numero", chooice, "è pari")
        else:
            print("Il numero", chooice, "è dispari")
    else:
        print("Non si è inserito un dato valido")
    
    chooice = input("Si vuole ripetere la scelta?")
    
    #si esce dal ciclo while
    if chooice.lower() == "no":
        break