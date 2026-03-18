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
   
class Fabbrica:
    
    def __init__(self, inventario, prod):
        self.inventario = inventario
        self.prod = prod
        
    def aggiungi_prodotto(self, prod, quantity):
        self.inventario[prod.nome] = quantity

    def vendi_prodotto(self, prod, quant):
        if prod.name in self.inventario and self.inventario[prod] >= quant:
            old_quant = self.inventario[prod]
            self.inventario[prod] -= quant
            gain = old_quant - self.inventario[prod]
            return self.prod.calcola_profitto() * gain
        else:
            print("Quantità o tipo del prodotto non disponibile")
    
    def resi_prodotto(self, prod, quant):
        if self.inventario[prod] == prod:
            self.inventario[prod] += quant
        else:
            print("Prodotto non disponibile")