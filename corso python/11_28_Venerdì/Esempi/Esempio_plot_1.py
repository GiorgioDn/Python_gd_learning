import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#configura Seaborn
sns.set_theme(style="darkgrid")

#crea alcuni dati
data = np.random.normal(size=100)

#crea un grafico
sns.histplot(data, kde=True)
plt.title('Distribuzione dei dati')
plt.show()