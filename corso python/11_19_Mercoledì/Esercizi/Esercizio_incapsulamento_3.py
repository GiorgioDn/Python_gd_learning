from export.Auto import Auto
from export.Furgone import Furgone
from export.Motocicletta import Motocicletta
from export.GestoreParcoVeicoli import GestoreParcoVeicoli

while True:
    
    print("Creare la propria auto inserendo marca, modello, anno, numero porte")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno: "))
    numero_porte = int(input("numero porte: "))
    
    auto = Auto(marca, modello, anno, False, 4)
    
    print("Creare il proprio furgone inserendo marca, modello, anno, capacità di carico")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno: "))
    capacita_carico = int(input("capacità carico: "))
    
    chooice = int(input("Selezionare: \n1. Aggiungere un veicolo\n2. Rimuovere un veicolo\n"))
    
    match chooice:
        case 1:
            pass
        case 2:
            pass
        case _:
            print("Scelta non valida")
    
    chooice = input("Si vuole effettuare una nuova prova?")
    
    if chooice.lower() == "no":
        break