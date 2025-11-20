class Teatro:
    def __init__(self, posti:list[Posto]): # type: ignore
        self.__posti = posti
        
    def aggiungi_posto(self, posto:Posto): # type: ignore
        return self.__posti.append(posto)
        
    def stampa_posti_occupati(self):
        for posti_occupati in self.__posti:
            if posti_occupati.get_occupato() == True:
                print(posti_occupati.prenota())
    
    def prenota_posto(self, numero:int, fila:str):
        for posti_occupati in self.__posti:
            if posti_occupati.get_numero() == numero and posti_occupati.get_fila() == fila:
                print(posti_occupati.prenota())