from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading the test dataset
data = load_iris()
X = data.data  #features
y = data.target  #labels

#splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

#creating the classification model
model = RandomForestClassifier(n_estimators=100, random_state=41)

#model training
model.fit(X_train, y_train)

#predicting labels for the test set
predictions = model.predict(X_test)

#calculating model accuracy
accuracy = accuracy_score(y_test, predictions)

print(f'Accuracy: {accuracy:.2f}')

#iris file data analysis
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

#no null values
df.info()

#columns to plot
cols_to_plot = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)", "target"]

#pairplot to visualize general characteristics in relation between each column
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

plt.title('Correlation Matrix', fontsize=5)
plt.show()