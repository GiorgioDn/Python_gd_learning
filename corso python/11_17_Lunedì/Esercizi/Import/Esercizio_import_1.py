class Vendita:
    def __init__(self, list_dati):
        self.list_dati = list_dati
    
    #converto i dati int
    def conversion(self):
        for n in range(len(self.list_dati)):
                self.list_dati[n] = int(self.list_dati[n])

    #calcolo il totale
    def total_sell(self):
        total = 0
        self.conversion()
        for sell in self.list_dati:
            total += sell
        return total

    #calcolo la media
    def average_sell(self):
        average = 0
        self.conversion()
        for sell in self.list_dati:
            average += sell
        average = average/len(self.list_dati)
        
        return average
    
    #restituisco i valori sopra la media
    def above_average(self):
        above_average_list = []
        average = self.average_sell()
        for sell in self.list_dati:
            if sell > average:
                above_average_list.append(sell)

        return above_average_list