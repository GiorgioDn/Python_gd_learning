from export.Veicolo import *
from export.GestoreFlotta import *

def main():
    
    list_veicoli = []
    
    gestore = GestoreFlotta(list_veicoli)
    
    camion = Camion("Df433k", 100, 4)
    
    print(camion.carica(150))
    
    print(camion.get_carico_attuale())
    
    camion.scarica()
    
    print(camion.get_carico_attuale())
    
    gestore.aggiungi_veicolo(camion)
    
       
    furgone = Furgone("Se230po", 150, "diesel")
    
    print(furgone.carica(50))
    
    print(furgone.get_carico_attuale())
    
    furgone.scarica()
    
    print(furgone.get_carico_attuale())
    
    gestore.aggiungi_veicolo(furgone)
    
    
    motocarro = Motocarro("As700kk", 150, 10)
    
    print(motocarro.carica(50))
    
    print(motocarro.get_carico_attuale())
    
    motocarro.scarica()
    
    print(motocarro.get_carico_attuale())
    
    gestore.aggiungi_veicolo(motocarro)
    
    costo = gestore.costo_totale_manutenzione()
    
    print(f"Il costo di manutenzione totale è: {costo}")
    
    print()
    
    gestore.stampa_veicoli()
    
    print()
    
    gestore.rimuovi_veicolo("Se230po")
    
    gestore.stampa_veicoli()
    
    
                
if __name__ == "__main__":
    main()
else: 
    print("È stato importato")