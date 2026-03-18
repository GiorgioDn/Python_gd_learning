from export.ImpiegatoRuoli import *


def main():
    
    impiegati = []
    
    while True:
        
        print("\n Impiegati azienda")
        print("1. Aggiungere impiegati fissi")
        print("2. Aggiungere impiegati a provvigione")
        print("3. Vedere stipendio degli impiegati")
        print("4. Esci")
        chooice = int(input("Scegli una opzione: "))
        
        match chooice:
            case 1:
                nome = input("Inserire il nome del dipendente: ")
                cognome = input("Inserire il cognome: ")
                stipendio = float(input("Inserire lo stipendio: "))

                impiegato_fisso = ImpiegatoFisso(nome, cognome, stipendio)
                impiegati.append(impiegato_fisso)

            case 2:
                nome = input("Inserire il nome del dipendente: ")
                cognome = input("Inserire il cognome: ")
                stipendio = float(input("Inserire lo stipendio: "))

                impiegato_a_provvigione = ImpiegatoAProvvigione(nome, cognome, stipendio)
                impiegati.append(impiegato_a_provvigione)

            case 3:
                for n in impiegati:
                    if type(n) == ImpiegatoAProvvigione:
                        provvigione = float(input("Il dipendente è a provvigione, inserire lo provvigione: "))
                        print(impiegato_a_provvigione.calcola_stipendio(provvigione))
                    else:
                        print(impiegato_fisso.calcola_stipendio())

            case 4:
                break
            case _:
                print("Scelta non valida")
                
if __name__ == "__main__":
    main()
else: 
    print("È stato importato")