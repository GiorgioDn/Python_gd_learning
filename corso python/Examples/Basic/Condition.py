#si fa selezionare il numero per verificare sl'if o l'else
numero = int(input("Selezionare un numero intero: "))

#se la condizione è vera viene restituito il codice dopo i due punti
if numero > 0: 
    print ("Il numero è positivo")
#se la prima condizione è falsa si può usare l'elif
elif numero < 0:
    print("Il numero è negativo")
#se l'if e gli elif non vengono verificati si usa il codice dell'else
else: 
    print("Il numero è 0")
    
#match confronta il valore con il case
comando = input("Inserisci un comando: ")

match comando:
    case "start":
        print("Avvio del programma")
    case "stop":
        print("Chiusura del programma")
    case "pausa":
        print("Programma in pausa")
    case _:
        print("Programma non riconosciuto")