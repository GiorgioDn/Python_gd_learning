from .module.Car import Auto
from .module.Van import Furgone
from .module.Motorcycle import Motocicletta
from .module.ManageVehicle import GestoreParcoVeicoli

while True:
    
    list_veicoli = []
    
    print("Creare la propria auto inserendo marca, modello, anno, numero porte")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno: "))
    numero_porte = int(input("numero porte: "))
    
    auto = Auto(marca, modello, anno, numero_porte)
    
    list_veicoli.append([auto])
    
    print("Creare il proprio furgone inserendo marca, modello, anno, capacità di carico")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno: "))
    capacita_carico = int(input("capacità carico: "))
    
    furgone = Furgone(marca, modello, anno, capacita_carico)
    
    list_veicoli.append([furgone])
    
    print("Creare il proprio motocicletta inserendo marca, modello, anno, tipo")
    marca = input("Marca: ")
    modello = input("Modello: ")
    anno = int(input("Anno: "))
    tipo = (input("Tipo: "))
    
    motocicletta = Motocicletta(marca, modello, anno, tipo)
    
    list_veicoli.append([motocicletta])
    
    gestore_parco = GestoreParcoVeicoli(list_veicoli)
    
    print(gestore_parco.lista_veicoli())
    
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