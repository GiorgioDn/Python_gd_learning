from .PayMethod import MetodoPagamenti

class CartaDiCredito(MetodoPagamenti):
    def __init__(self, numero_carta:str, scadenza:str, cvv:int):
        self.__numero_carta = numero_carta
        self.__scadenza = scadenza
        self.__cvv = cvv
        
    def get_numero_carta(self):
        return self.__numero_carta
    
    def get_scadenza(self):
        return self.__scadenza
    
    def get_cvv(self):
        return self.__cvv
    
    def effettua_pagamento(self, importo:float):
        if len(self.__numero_carta) > 16:
            if int(self.__numero_carta) != ValueError:
                if len(self.__cvv) == 3:
                    return f"È stato effettuato il pagamento con carta con il seguente importo: {importo} euro"
        else: 
            return False

class PayPal(MetodoPagamenti):
    def __init__(self, account:str):
        self.__account = account
        
    def get_account(self):
        return self.__account
    
    def effettua_pagamento(self, importo:float):
        return f"È stato eseguito il pagamenti di {importo} euro con Paypal"


class BonificoBancario(MetodoPagamenti):
    def __init__(self, iban:str, swift:str):
        self.__iban = iban
        self.__swift = swift
    
    def get_swift(self):
            return self.__swift  
        
    def get_iban(self):
            return self.__iban
        
    def effettua_pagamento(self, importo:float):
        if len(self.__iban) > 27:
            return f"È stato eseguito il bonifico di {importo} euro"
        else: 
            return False
        
    
    
