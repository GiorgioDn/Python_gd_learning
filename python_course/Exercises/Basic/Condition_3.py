#selezione dei due numeri int dall'utente
print ("Selezionare due numeri")
num1 = float(input("Primo numero: "))
num2 = float(input("Secondo numero: "))

#Scrivo le operazioni disponibili e le faccio scegliere all'utente
print("Selezionare il numero dell'operazione corrispondente tra: \n 1. Addizione \n 2. Sottrazione \n 3. Moltiplicazione \n 4. Divisione")
operazione = int(input())

#associo l'operazione corrispondente in base all'input dell'utente
match operazione:
    case 1: 
        operazione = num1 + num2
        print("L'addizione ha restituito: ", operazione)
    case 2: 
        operazione = num1 - num2
        print("La sottrazione ha restituito: ", operazione)
    case 3: 
        operazione = num1 * num2
        print("La moltiplicazione ha restituito: ", operazione)
    case 4: 
        #controllo che la divisione possa essere eseguita
        if num2 == 0:
            print("Errore divisione per zero")
        else: 
            operazione = num1 / num2
            print("La divisione ha restituito: ", operazione)
    case _:
        print("Operazione non valida")