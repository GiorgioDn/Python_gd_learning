from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

#loading the test dataset
data = load_iris()
X = data.data  #features
y = data.target  #labels

#data normalization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

#creating the classification model
model = KNeighborsClassifier(leaf_size=60, n_jobs=2)

#model training
model.fit(X_train, y_train)

#predicting labels for the test set
predictions = model.predict(X_test)

#calculating model accuracy
accuracy = accuracy_score(y_test, predictions)

print(f'Accuracy: {accuracy:.10f}')

#printing a metric comparing test values with predicted ones
score = classification_report(y_test, predictions)
print(score)