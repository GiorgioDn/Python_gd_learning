#istanzio una classe ristorante
class Ristorante:
    
    #attributi della classe
    #indica lo stato di apertura
    open = False
    #dizionario contenente il menu
    '''
    #DATI DI PROVA
    menu = {
        "margherita": "3€", 
        "ortolana": "4€", 
        "funghi": "4€", 
        "diavola": "4,50€",  
    }
    '''
    
    menu = {}
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina

    #metodo descrive il ristorante
    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} è specializzato in {self.tipo_cucina}")
        
    #metodo che mostra lo stato di apertura in base all'attributo open
    def stato_apertura(self):
        if self.open == True:
            print("Il ristorante è ancora aperto")
        else:
            print("Il ristorante è ancora chiuso")
        
    #metodo per aprire il ristorante ed impostarer open su true
    def apri_ristorante(self):
        if self.open == True:
            self.stato_apertura()
        else: 
            self.open = True
            print("Il ristorante è ora aperto")
         
    #metodo per aprire il ristorante ed impostarer open su false   
    def chiudi_ristorante(self):
        if self.open == False:
            self.stato_apertura()
        else: 
            self.open = False
            print("Il ristorante è ora chiuso")
            
    #metodo per aggiungere al menu
    def aggiungi_al_menu(self, nome_piatto, price):
        self.menu[nome_piatto] = price
    
    #metodo per togliere al menu
    def togli_dal_menu(self, nome_piatto):
        self.menu.pop(nome_piatto)
        
    #metodo per stampare il menu singolarmente
    def stampa_menu(self):
        print("Il menù è il seguente: ")
        for k, v in self.menu.items():
            print(f"{k} : {v}")

'''
#TEST METODI      
ristorante = Ristorante("Ristoro", "pizza")

ristorante.descrivi_ristorante()

ristorante.stato_apertura()

ristorante.apri_ristorante()

ristorante.stato_apertura()

ristorante.chiudi_ristorante()

ristorante.stato_apertura()

ristorante.stampa_menu()

ristorante.aggiungi_al_menu("marinara", "3€")

ristorante.aggiungi_al_menu("bufala", "3€")

ristorante.stampa_menu()

ristorante.togli_dal_menu("marinara")

ristorante.stampa_menu()

'''

while True:
    
    #dichiaro il ristorante
    print("Digitare il nome del ristorante ed il tipo di cucina che si vuole aggiungere")
    nome = input("Nome del ristorante: ")
    tipo_cucina = input("Tipo di cucina: ")
    
    ristorante = Ristorante(nome, tipo_cucina)
    
    ristorante.descrivi_ristorante()
    
    ristorante.stato_apertura()
    
    #creo i piatti da aggiungere al menu
    print("Aggiungere nel menu i tipi di piatto con i relativi prezzi")
    while True:
        nome_piatto = input("Nome piatto: ")
        price = float(input("Prezzo: "))
        
        ristorante.aggiungi_al_menu(nome_piatto, price)
        
        chooice = input("Si vuole aggiungere altri piatti? ")
        #si esce dal ciclo while
        if chooice.lower() == "no":
            break
    
    ristorante.stampa_menu()
    
    #scelgo uno dei metodi da usare
    chooice = int(input("Selezionare l'operazione da fare: \n1. Aggiungere al menu \n2.Rimuovere dal menu \n3. Modificare apertura \n4. Stamapre il menu\n"))
    
    match chooice:
        case 1:
            print("Aggiungere nel menu i tipi di piatto con i relativi prezzi")
            nome_piatto = input("Nome piatto: ")
            price = float(input("Prezzo: "))
        
            ristorante.aggiungi_al_menu(nome_piatto, price)
            
            ristorante.stampa_menu()
        case 2:
            print("Rimuovere il piatto")
            nome_piatto = input("Nome piatto: ")
            
            ristorante.togli_dal_menu(nome_piatto)
            
            ristorante.stampa_menu()
        case 3:
            chooice = input("Selezionare se il ristorante è aperto o chiuso")
            if chooice.lower() == "aperto":
                ristorante.apri_ristorante()
            else: 
                ristorante.chiudi_ristorante()
        case 4:
            ristorante.stampa_menu()
        case _:
            print("Operazione non disponibile")
    
    chooice = input("Si vuole ripetere la scelta? ")
    #si esce dal ciclo while
    if chooice.lower() == "no":
        break