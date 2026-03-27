import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#configure Seaborn
sns.set_theme(style="darkgrid")

#create some data
data = np.random.normal(size=100)

#create a plot
sns.histplot(data, kde=True)
plt.title('Data Distribution')
plt.show()