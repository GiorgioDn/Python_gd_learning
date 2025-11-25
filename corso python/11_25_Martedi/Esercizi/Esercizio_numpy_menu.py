import numpy as np

def main():
    
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
        print("6. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        match chooice:
            case 1:
                with open (txt, "a") as file:
                    file.write(string)
            case 2:
                with open (txt, "a") as file:
                    file.write(string)
            case 3:
                with open (txt, "a") as file:
                    file.write(string)
            case 4:
                with open (txt, "a") as file:
                    file.write(string)
            case 5:
                with open (txt, "a") as file:
                    file.write(string)
            case 6:
                with open (txt, "a") as file:
                    file.write(string)
            case 7:
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