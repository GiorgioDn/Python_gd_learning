from Import.Import_1 import Sell

while True: 
    
    dati_vendita = []
    
    print("Inserire importi vendite")
    
    while True:
        dati = input("Importo: ")
        dati_vendita.append(dati)
        
        chooice = input("Si vuole selezionare un altro importo? ")
    
        #si esce dal ciclo while
        if chooice.lower() == "no":
            break
        
    vendita = Vendita(dati_vendita)
    
    x = vendita.total_sell()
    
    print(x)
    
    chooice = input("Si vuole ripetere la scelta? ")
    
    #si esce dal ciclo while
    if chooice.lower() == "no":
        break