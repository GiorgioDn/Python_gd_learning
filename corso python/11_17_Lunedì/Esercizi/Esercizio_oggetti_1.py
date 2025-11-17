#definisco la classe punto
class Punto:
    #definisco il metodo costruttore che prenderà le coordinate del punto
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #metodo muovi: cambia le coordinate
    def muovi(self, dx, dy):
        self.x = dx 
        self.y = dy
    #metodo distanza da origine: calcola la distanza tra il punto e l'origine
    def distanza_da_origine(self):
        distance = (self.x**2 + self.y**2)**0.5
        return distance

while True:
    #inserisco i dati per istanziare la classe
    print("Selezionare le coordinate del punto")
    x = int(input("Punto x: "))
    y = int(input("Punto y: "))
    
    point = Punto(x, y)
    
    chooice = int(input("Quale operazione si vuole effettuare tra: \n1. Stampa le coordinate \n2. Muovere le coordinate \n3. Distanza dall'origine\n"))
    
    #scelta dei metodi dichiariati nella classe
    match chooice:
        case 1:
            print(f"Coordinata x = {point.x} \nCoordinata y = {point.y}")
        case 2:
            print("Selezionare le nuove coordinate del punto")
            x = int(input("Punto x: "))
            y = int(input("Punto y: "))
            point.muovi(x, y)
            print(f"Nuova coordinata x = {point.x} \n Nuova coordinata y = {point.y}")
        case 3:
            distance = point.distanza_da_origine()
            print(f"La distanza dall'origine è: {distance}")
        case _:
            print("Scelta non valida")
    
    chooice = input("Si vuole ripetere la scelta? ")
    
    #si esce dal ciclo while
    if chooice.lower() == "no":
        break