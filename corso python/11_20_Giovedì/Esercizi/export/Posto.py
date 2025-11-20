class Posto:
    #definisco la classe posto con parametri int e stringa
    def __init__(self, numero:int, fila:str):
        self.__numero = numero
        self.__fila = fila
        #imposto inizialmente l'attributo a False
        self.__occupato = False 
    
    #uso solamente i get perchè i dati non sono modificabili
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila
    
    def get_occupato(self):
        return self.__occupato
    
    #metodo prenotazione per gestire le prenotazioni
    def prenota(self):
        if self.__occupato == False:
            self.__occupato = True
            return f"Il posto numero: {self.__numero} in fila: {self.__fila} è stato prenotato"
        else:
            return f"Il posto numero: {self.__numero} in fila: {self.__fila} è occupato"
    
    #metodo per liberare il posto e scambiare lo stato di occupato
    def libera(self):
        if self.__occupato == True:
            self.__occupato = False
            return f"Il posto numero: {self.__numero} in fila: {self.__fila} è stato liberato"
        else:
            return f"Il posto numero: {self.__numero} in fila: {self.__fila} è libero"