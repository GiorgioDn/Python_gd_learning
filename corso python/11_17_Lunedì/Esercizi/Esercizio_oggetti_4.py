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