from .module.BankAccount import ContoBancario

while True:
    
    print("Registrarsi con il nome del titolare e quanto è il saldo iniziale")
    titolare = input("Titolare: ")
    saldo = float(input("Saldo: "))     
    
    conto = ContoBancario(titolare, saldo)
    
    titolare = conto.get_titolare()
    
    while True:
        if titolare == False:
            titolare = input("Nome non presente, bisogna selezionare un nome per il titolare: ")
            conto.set_titolare(titolare)
            titolare = conto.get_titolare()
        else:
            break
        
    print(f"Il titolare del conto è: {titolare}")
    
    saldo = conto.visualizza_saldo()
    
    print(f"Il saldo attuale ammonta a {saldo} euro")
    
    chooice = int(input("Selezionare 1 per depositare 2 per prelevare: "))
    
    match chooice:
        case 1:
            chooice = float(input("Selezionare la cifra da depositare: "))
            deposit = conto.deposita(chooice)
            while True:
                if deposit == False:
                    chooice = float(input("Cifra non valida selezionare la nuova cifra da depositare: "))
                    deposit = conto.deposita(chooice)
                else: 
                    break
            saldo = conto.visualizza_saldo()
            print(f"Il saldo attuale ammonta a {saldo} euro")
            
        case 2:
            chooice = float(input("Selezionare la cifra da prelevare: "))
            withdraw = conto.preleva(chooice)
            while True:
                if withdraw == False:
                    if chooice > conto.visualizza_saldo():
                        chooice = float(input("Saldo non sufficiente selezionare la nuova cifra da prelevare: "))
                        withdraw = conto.preleva(chooice)
                    else:
                        chooice = float(input("Cifra non valida selezionare la nuova cifra da prelevare: "))
                        withdraw = conto.preleva(chooice)
                else: 
                    break
            saldo = conto.visualizza_saldo()
            print(f"Il saldo attuale ammonta a {saldo} euro")
        case _:
            print("Scelta non valida")
    
    chooice = input("Si vuole effettuare un accesso con una persona diversa?")
    
    if chooice.lower() == "no":
        break