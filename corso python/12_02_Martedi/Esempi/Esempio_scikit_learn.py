from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#caricamento del dataset di prova
data = load_iris()
X = data.data  #caratteristiche
y = data.target  #etichette

#divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

#creazione del modello di classificazione
model = RandomForestClassifier(n_estimators=100, random_state=41)

#addestramento del modello
model.fit(X_train, y_train)

#predizione delle etichette per il set di test
predictions = model.predict(X_test)

#calcolo dell'accuratezza del modello
accuracy = accuracy_score(y_test, predictions)

print(f'Accuracy: {accuracy:.2f}')

#analisi dati file iris
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

#non si hanno valori nulli
df.info()

#colonne da mettere come grafico
cols_to_plot = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)", "target"]

#grafico pairplot per visualizzare le caratteristiche generali in realzione tra ogni colonna
g = sns.pairplot(df[cols_to_plot], diag_kind='kde', plot_kws={'alpha': 0.5, 's': 15}, diag_kws={'fill': True}, height=2)

g.figure.set_size_inches(12, 8)
g.figure.suptitle('Pairplot Matrix')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(
    df.corr(),
    annot=True,
    cmap='coolwarm',
    center=0,
    linewidths=0.5,
    linecolor='white',
    fmt=".2f"
)

plt.title('Matrice di Correlazione', fontsize=5)
plt.show()