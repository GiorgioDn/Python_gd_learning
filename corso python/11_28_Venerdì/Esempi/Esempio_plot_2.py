import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

#crea la figura vuota
plt.figure()
#imposta le coordinarte x e y
plt.plot(x, y)
#titolo del grafico
plt.title('Grafico a Linee')
#nome dell'asse x
plt.xlabel('X Axis')
#nome dell'asse y
plt.ylabel('Y Axis')
#visualizza il grafico
plt.show()

#crea il grafico a barre
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()

#istogramma
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()