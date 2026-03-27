class Sell:
    def __init__(self, list_dati):
        self.list_dati = list_dati
    
    #convert data to int
    def conversion(self):
        for n in range(len(self.list_dati)):
                self.list_dati[n] = int(self.list_dati[n])

    #calculate total
    def total_sell(self):
        total = 0
        self.conversion()
        for sell in self.list_dati:
            total += sell
        return total

    #calculate average
    def average_sell(self):
        average = 0
        self.conversion()
        for sell in self.list_dati:
            average += sell
        average = average/len(self.list_dati)
        
        return average
    
    #return values above average
    def above_average(self):
        above_average_list = []
        average = self.average_sell()
        for sell in self.list_dati:
            if sell > average:
                above_average_list.append(sell)

        return above_average_list