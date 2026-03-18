#variabile di input per il numero selezionato dall'utente
numero = int(input("Selezionare un numero intero: "))

#verifico il numero in base alle condizoni soddisfatte
if numero > 0:
    if numero%2 == 0:
        if numero > 10:
            print("Il numero è pari e maggiore di 10")
        else:
            print("Il numero è pari e minore di 10")
    else:
        print("Il numero è dispari")
else:
    print("Il numero è negativo")