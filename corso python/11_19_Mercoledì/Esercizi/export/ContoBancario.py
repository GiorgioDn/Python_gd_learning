class ContoBancario:
    
    #la classe prende in input una stringa ed un float e li assegna come valori privati
    def __init__(self, titolare:str, saldo:float):
        self.__titolare = titolare
        self.__saldo = saldo
    
    #visualizza la variabile privata titolare
    def get_titolare(self):
        if len(self.__titolare) > 0:
            return self.__titolare
        else:
            return False
    
    #modifica il valore della variabile privata titolare
    def set_titolare(self, titolare:str):
        if len(titolare) > 0:
            self.__titolare = titolare
        else:
            return False
    
    #aumenta il saldo in base al valore float inserito
    def deposita(self, importo:float):
        if importo > 0:
            self.__saldo += importo
        else:
            return False

    #diminuisce il saldo in base al valore float inserito
    def preleva(self, importo:float):
        if importo > 0 and self.__saldo >= importo:   
            self.__saldo -= importo
        else:
            return False
    
    #visualizza la variabile privata saldo
    def visualizza_saldo(self):
        return self.__saldo