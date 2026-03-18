from export.Officina import Officina
from export.TicketRiparazione import TicketRiparazione
from export.ElettrodomesticoSpecifico import *
from random import randint

def main():
    
    officina = Officina("Ripara", [])
    
    while True:
        
        print("\n Inserire gli oggetti da riparare")
        print("1. Lavatrice ")
        print("2. Frigorifero")
        print("3. Forno")
        print("4. Ticket aperti")
        print("5. Chiudi un ticket")
        print("6. Totale preventivo")
        print("7. Statistiche preventivi")
        print("8. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        match chooice:
            case 1:
                extra = []
                marca = input("Inserire la marca della lavatrice: ")
                modello = input("Inserire il modello della lavatrice: ")
                anno_acquisto = int(input("Inserire l'anno di acquisto della lavatrice: "))
                guasto = input("Descrivere il guasto: ")
                capacita = int(input("Capacità della lavatrice: ")) 
                giri = int(input("Giri centrifuga della lavatrice: "))
                
                lavatrice = Lavatrice(marca, modello, anno_acquisto, guasto, capacita, giri)
                
                chooice = input("Ci sono altri costi? si/no")
                if chooice.lower() == "si":
                    while True:
                        extra_costo = float(input("Aggiungere il valore del costo extra: "))
                        extra.append(extra_costo)
                        chooice = input("Ci sono altri costi? si/no")
                        if chooice.lower() == "no":
                            break
                
                id = str(randint(0, 999999999999))
                
                tickets = TicketRiparazione(id, lavatrice)
                
                tickets.calcola_preventivo(extra)
                
                officina.aggiungi_ticket(tickets)

            case 2:
                extra = []
                marca = input("Inserire la marca della frigorifero: ")
                modello = input("Inserire il modello della frigorifero: ")
                anno_acquisto = int(input("Inserire l'anno di acquisto della frigorifero: "))
                guasto = input("Descrivere il guasto: ")
                litri = int(input("Litri che può avere: "))
                freezer = input("Ha freezer? si/no ")
                
                if freezer.lower() == "si":
                    freezer = True
                else:
                    freezer = False
                
                frigorifero = Frigorifero(marca, modello, anno_acquisto, guasto, litri, freezer)
                
                chooice = input("Ci sono altri costi? si/no")
                if chooice.lower() == "si":
                    while True:
                        extra_costo = float(input("Aggiungere il valore del costo extra: "))
                        extra.append(extra_costo)
                        chooice = input("Ci sono altri costi? si/no")
                        if chooice.lower() == "no":
                            break
                
                id = str(randint(0, 999999999999))
                
                tickets = TicketRiparazione(id, frigorifero)
                
                tickets.calcola_preventivo(extra)
                
                officina.aggiungi_ticket(tickets)
                
            case 3:
                extra = []
                marca = input("Inserire la marca della forno: ")
                modello = input("Inserire il modello della forno: ")
                anno_acquisto = int(input("Inserire l'anno di acquisto della forno: "))
                guasto = input("Descrivere il guasto: ")
                alimentazione = input("Dire se è elettrico o a gas: ")
                ventilato = input("È ventilato? si/no")
                
                if ventilato.lower() == "si":
                    ventilato = True
                else:
                    ventilato = False
                
                forno = Forno(marca, modello, anno_acquisto, guasto, alimentazione, ventilato)
                
                chooice = input("Ci sono altri costi? si/no")
                if chooice.lower() == "si":
                    while True:
                        extra_costo = float(input("Aggiungere il valore del costo extra: "))
                        extra.append(extra_costo)
                        chooice = input("Ci sono altri costi? si/no")
                        if chooice.lower() == "no":
                            break
                
                id = str(randint(0, 999999999999))
                
                tickets = TicketRiparazione(id, forno)
                
                tickets.calcola_preventivo(extra)
                
                officina.aggiungi_ticket(tickets)
                
            case 4:
                officina.stampa_ticket_aperti()
            case 5:
                pass
            case 6:
                print(officina.totale_preventivi())
            case 7:
                pass
            case 8:
                break
            case _:
                print("Scelta non valida")
                
if __name__ == "__main__":
    main()
else: 
    print("È stato importato")