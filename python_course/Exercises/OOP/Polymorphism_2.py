from export.Teatro import *
from export.PostoSpeciale import *

def main():
    
    teatro = Teatro([])   
    
    while True:
        
        print("\n Selezionare l'operazione da effettuare")
        print("1. Aggiungere un posto standard")
        print("2. Aggiungere un posto vip")
        print("3. Visualizzare i posti occupati")
        print("4. Prenotare il posto")
        print("5. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        match chooice:
            case 1:
                numero = int(input("Numero: "))
                fila = input("Fila: ")
                costo = input("Costo: ")
                
                posto_standard = PostoStandard(numero, fila, costo)
                teatro.aggiungi_posto(posto_standard)
                
            case 2:
                servizi = []
                numero = int(input("Numero: "))
                fila = input("Fila: ")
                costo = input("Costo: ")
                print("Aggiungere 2 servizi speciali")
                for n in range(2):
                    servizio = input("Servizio: ")
                    servizi.append(servizio)
                
                posto_standard = PostoVIP(numero, fila, costo, servizi)
                teatro.aggiungi_posto(posto_standard)
            case 3:
                teatro.stampa_posti_occupati()
            case 4:
                numero = int(input("Numero Posto: "))
                fila = input("Fila Posto: ")
                teatro.prenota_posto(numero, fila)
            case 5:
                break
            case _:
                print("Scelta non valida")
                
if __name__ == "__main__":
    main()
else: 
    print("È stato importato")