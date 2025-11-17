#classe prodotto
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione= costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    #metodo che usa i parametri del prodotto  
    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto
    
class Abbigliamento:
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.nome = self.prodotto.nome
        self.costo_produzione= self.prodotto.costo_produzione
        self.prezzo_vendita = self.prodotto.prezzo_vendita
        self.materiale = materiale
    #metodo che usa la classe prodotto  
    def calcola_profitto(self):
        return self.prodotto.calcola_profitto()
    
class Abbigliamento:
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.nome = self.prodotto.nome
        self.costo_produzione= self.prodotto.costo_produzione
        self.prezzo_vendita = self.prodotto.prezzo_vendita
        self.garanzia = garanzia
    #metodo che usa la classe prodotto  
    def calcola_profitto(self):
        return self.prodotto.calcola_profitto()
    

        