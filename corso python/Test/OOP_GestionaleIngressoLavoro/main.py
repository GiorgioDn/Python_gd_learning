from module.RuoloDipendenti import *
from module.Azienda import *

def main():
    
    azienda = Azienda("Classe Academy python")
    
    while True:
        
        print("\n Selezionare l'opzione da fare in azienda")
        print("1. Aggiungere un impiegato")
        print("2. Aggiungere un amministratore")
        print("3. Aggiungere un direttore")
        print("4. Aggiungere i dipartimenti")
        print("5. Vedere i dipendenti")
        print("6. Vedere i diaprtimenti")
        print("7. Verificare gli ingressi")
        print("8. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        match chooice:
            case 1:
                badge = []
                turni = []
                info = input("Inserire il nome per il badge: ")
                badge.append(info)
                
                info = input("Inserire il cognome per il badge: ")
                badge.append(info)
                
                info = input("Inserire il ruolo per il badge: ")
                badge.append(info)
                
                info = input("Inserire il nome azienda per il badge: ")
                badge.append(info)
                
                info = float(input("Inserire l'orario di entrata: "))
                turni.append(info)
                
                info = float(input("Inserire l'orario di uscita: "))
                turni.append(info)
                
                impiegato = Impiegato(badge, turni)
                
                azienda.aggiungi_dipendente(impiegato)
                
            case 2:
                badge = []
                turni = []
                info = input("Inserire il nome per il badge: ")
                badge.append(info)
                
                info = input("Inserire il cognome per il badge: ")
                badge.append(info)
                
                info = input("Inserire il ruolo per il badge: ")
                badge.append(info)
                
                info = input("Inserire il nome azienda per il badge: ")
                badge.append(info)
                
                info = float(input("Inserire l'orario di entrata: "))
                turni.append(info)
                
                info = float(input("Inserire l'orario di uscita: "))
                turni.append(info)
                
                info = input("Inserire il dipartimento di competenza: ")
                
                amministratore = Amministratore(badge, turni, info)
                
                azienda.aggiungi_dipendente(amministratore)
            case 3:
                badge = []
                turni = []
                dipartimenti = []
                info = input("Inserire il nome per il badge: ")
                badge.append(info)
                
                info = input("Inserire il cognome per il badge: ")
                badge.append(info)
                
                info = input("Inserire il ruolo per il badge: ")
                badge.append(info)
                
                info = input("Inserire il nome azienda per il badge: ")
                badge.append(info)
                
                info = float(input("Inserire l'orario di entrata: "))
                turni.append(info)
                
                info = float(input("Inserire l'orario di uscita: "))
                turni.append(info)
                
                for n in range(3):
                    info = input("Inserire il dipartimento di competenza: ")
                    dipartimenti.append(info)
                
                direttore = Direttore(badge, turni, dipartimenti)
                
                azienda.aggiungi_dipendente(direttore)
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("Scelta non valida")
                
if __name__ == "__main__":
    main()
else: 
    print("È stato importato")