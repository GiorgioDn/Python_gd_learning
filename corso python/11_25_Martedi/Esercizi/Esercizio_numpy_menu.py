import numpy as np

def main():
    
    #creazione id utente
    rand_id = str(np.random.randint(0, 100, 10))
    txt = "corso python/11_25_Martedi/Esercizi/export/dati_2.txt"
    #crea o inizializza il file se già esistente
    with open (txt, "w") as file:
        string = f"{rand_id}\n" 
        file.write(string)
    
    while True:
        
        #legge la prima riga
        file = open(txt, "r")
        riga = file.readline().strip()
        file.close()
        #sovrascrive il file se non è presente lo stesso id
        if riga != rand_id:
            string = f"{rand_id}\n"  
            file = open (txt, "w")
            file.write(string)
            file.close()
        
        print("\n Scegliere l'operazione da effettuare: ")
        print("1. Creare una nuova matrice 2D")
        print("2. Estrarre e stampare la sotto-matrice centrale")
        print("3. Trasporre la matrice e stamparla")
        print("4. Calcolare e stampare la somma di tutti gli elementi della matrice")
        print("5. Moltiplicazione con un'altra matrice")
        print("6. Media degli elementi della matrice")
        print("7. Determinante della matrice")
        print("8. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        match chooice:
            case 1:
                start = int(input("Selezionare il valore di partenza della matrice: "))
                end = int(input("Selezionare il valore finale della matrice: "))
                row = int(input("Selezionare il numero di righe della matrice: "))
                col = int(input("Selezionare il numero di colonne della matrice: "))
                
                matrix = np.random.randint(start, end, size=(row, col))
                string = f"Matrice 2d: \n{matrix}\n"
                print(matrix)
                with open (txt, "a") as file:
                    file.write(string)
            case 2:
                
                #creazione della sottomatrice centrale
                sub_matrix = matrix[1: row-1, 1: col-1]
                string = f"Sottomatrice centrale: \n{sub_matrix}\n"
                print(sub_matrix)
                with open (txt, "a") as file:
                    file.write(string)
            case 3:
                
                #creazione della matrice trasposta
                transpose_matrix = matrix.transpose()
                string = f"Trasposta della matrice: \n{transpose_matrix}\n"
                print(transpose_matrix)
                with open (txt, "a") as file:
                    file.write(string)
            case 4:
                
                #somma degli elementi della matrice
                sum = matrix.sum()
                string = f"Somma degli elementi della matrice: \n{sum}\n"
                print(sum)
                with open (txt, "a") as file:
                    file.write(string)
            case 5:
                
                print("Inserire i dati della seconda matrice")
                #creazione seconda matrice 
                start = int(input("Selezionare il valore di partenza della matrice: "))
                end = int(input("Selezionare il valore finale della matrice: "))
                second_matrix = np.random.randint(start, end, size=(row, col))
                
                #creo la matrice con cui moltiplicare elemento per elemento
                #matmul fa il prodotto riga per colonna
                #mult_matrix = np.matmul(matrix, second_matrix)
                #moltiplica elemento per elemento
                mult_matrix = matrix * second_matrix
                string = f"Seconda matrice: \n{second_matrix}\nProdotto tra le matrici: \n{mult_matrix}\n"
                print(mult_matrix)
                with open (txt, "a") as file:
                    file.write(string)
            case 6:
                
                #media degli elementi della matrice
                mean = matrix.mean()
                string = f"Media degli elementi della matrice: \n{mean}\n"
                print(mean)
                with open (txt, "a") as file:
                    file.write(string)
                    
            case 7:
                
                #controllo matrice quadrata
                if row == col:
                    #determinante della matrice
                    det = np.linalg.det(matrix)
                    string = f"determinante della matrice: \n{det}\n"
                    print(det)
                    with open (txt, "a") as file:
                        file.write(string)
                else:
                    print("La matrice non è quadrata")
                
            case 8:
                
                #scelta se cambiare utente o uscire
                chooice = input("Si vuole inserire dati come nuovo utente? si/no: ")
                if chooice.lower() == "si":
                    rand_id = str(np.random.randint(0, 100, 10))
                else:
                    break
            case _:
                print("Scelta non valida")
                
if __name__ == "__main__":
    main()
else: 
    print("È stato importato")