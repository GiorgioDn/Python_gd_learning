#selezione dei numeri dall'utente che andranno a popolare la lista
lista_num = []
print ("Selezionare i numeri")
#aggiungo gli input alla lista man mano che vengono digitati dall'utente
num = float(input("Primo numero: "))
lista_num.append(num)
num = float(input("Secondo numero: "))
lista_num.append(num)
num = float(input("Terzo numero: "))
lista_num.append(num)
num = float(input("Quarto numero: "))
lista_num.append(num)
num = float(input("Quinto numero: "))
lista_num.append(num)

#Scrivo le operazioni disponibili e le faccio scegliere all'utente
print("Selezionare il numero dell'operazione corrispondente tra: \n 1. Addizione \n 2. Sottrazione \n 3. Moltiplicazione \n 4. Divisione")
operazione = int(input())

#associo l'operazione corrispondente in base all'input dell'utente
match operazione:
    case 1: 
        operazione = lista_num[0] + lista_num[1] + lista_num[2] + lista_num[3] + lista_num[4]
        print("L'addizione ha restituito: ", operazione)
    case 2: 
        operazione = lista_num[0] - lista_num[1] - lista_num[2] - lista_num[3] - lista_num[4]
        print("La sottrazione ha restituito: ", operazione)
    case 3: 
        operazione = lista_num[0] * lista_num[1] * lista_num[2] * lista_num[3] * lista_num[4]
        print("La moltiplicazione ha restituito: ", operazione)
    case 4: 
        #controllo che la divisione possa essere eseguita
        if lista_num[0] == 0 or lista_num[1] == 0 or lista_num[2] == 0 or lista_num[3] == 0 or lista_num[4] == 0:
            print("Errore divisione per zero")
        else: 
            operazione = lista_num[0] / lista_num[1] / lista_num[2] / lista_num[3] / lista_num[4]
            print("La divisione ha restituito: ", operazione)
    case _:
        print("Operazione non valida")