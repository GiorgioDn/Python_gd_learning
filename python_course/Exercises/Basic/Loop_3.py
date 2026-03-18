#variabili per inizializzare i numeri selezionati, pari, dispari e le relative somme
even = []
odd = []

#lista input utenti 
remember = []

#while per gli input positivi dell'utente
while True:
    num_int = int(input("Digitare un numero intero positivo maggiore di 0: "))
    
    #ciclo while eseguito finchè il numero non è positivo
    while num_int<=0:
        num_int = int(input("Digitare un numero intero positivo maggiore di 0: "))

    print("Il numero scelto è: ", num_int)
    remember.append(num_int)
    
    #variabili per la somma
    even_sum = 0
    odd_sum = 0

    #verifico la parità e disparità del numero selezionato
    for n in range(1, num_int):
        if n%2==0:
            even.append(n)
            even_sum += n
        else:
            odd.append(n)
            odd_sum += n
            
    print("I numeri pari nell'intervallo sono: ", even, "la cui somma è: ", even_sum)
            
    print("I numeri dispari nell'intervallo sono: ", odd, "la cui somma è: ", odd_sum)

    #verifico che il numero sia primo oppure no 
    if num_int < 2:
        print("Il numero selezionato non è primo")
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if num_int % i == 0:
                print("Il numero selezionato non è primo")
                break
        else:
            print("Il numero selezionato è primo")
    
    print("I numeri scelti finora sono:", remember)
    chooice = input("Si desidera continuare ad inserire numeri? ")
    
    if chooice.lower() == "no":
        break
    #azzero le variabili usate per riutilizzarle nel nuovo ciclo
    else:
        even.clear()
        odd.clear()
