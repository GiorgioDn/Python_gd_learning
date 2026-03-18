from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

#caricamento del dataset di prova
data = load_iris()
X = data.data  #caratteristiche
y = data.target  #etichette

#normalizzazione dati
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

#creazione del modello di classificazione
model = KNeighborsClassifier(leaf_size=60, n_jobs=2)

#addestramento del modello
model.fit(X_train, y_train)

#predizione delle etichette per il set di test
predictions = model.predict(X_test)

#calcolo dell'accuratezza del modello
accuracy = accuracy_score(y_test, predictions)

print(f'Accuracy: {accuracy:.10f}')

#stampa una metrica confrontando i valori di test con quelli predetti
score = classification_report(y_test, predictions)
print(score)