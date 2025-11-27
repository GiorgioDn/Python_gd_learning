import pandas as pd
import numpy as np

file_path = "corso python/11_27_Giovedi/Esercizi/dataset/tele.csv"

#creazione del dataset dal file
df = pd.read_csv(file_path)
print("\n=====TABELLA INIZIALE=====\n")
print(df)

#filtro colonne numeriche
numbers = df.select_dtypes(include=["float64", "int64"])
print(numbers)

#describe: statistiche descrittive
print("\n=====DESCRIBE TABELLA=====\n")
desc = df.describe()
print(desc)

#info: sintesi del DataFrame
print("\n=====INFO TABELLA=====\n")
desc = df.info()
print(desc)

#value count: numero occorrenze per riga
print("\n=====VALUE COUNTS TABELLA=====\n")
val_count = df.value_counts()
print(val_count)

#rimozione o sostituzione
print("\n=====CORREZIONE ANOMALIE E VALORI NULLI=====\n")
for col in numbers.columns:
    median = df[col].median()
    if col == "ID_Cliente":
        rand_id = np.random.randint(10000000, 99999999)
        df[col] = df[col].fillna(rand_id)
    elif col == "Età":
        df.loc[(df[col] < 0) | (df[col] > 100), "Età"] = np.nan
        df[col] = df[col].fillna(median)
    elif col == "Durata_Abbonamento":
        df.loc[df["Durata_Abbonamento"] < 0, "Durata_Abbonamento"] = 0
        df[col] = df[col].fillna(0)
    elif col == "Dati consumati":
        df.loc[df[col] <= 0, "Dati_Consumati"] = np.nan
        df[col] = df[col].fillna(median)
    else: 
        df[col].dropna()

df = df.dropna(subset=["Churn"])
    
print(df)

#creazione costo per gb 
print("\n=====COLONNA COSTO PER GB=====\n")
df["Costo_Per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"]
print(df)

#conversione churn in numerico
print("\n=====CONVERSIONE CHURN IN NUMERICO=====\n")
df["Churn"] = df["Churn"].replace({"Sì": 1, "No": 0})
print(df)

#relazione groupby
print("\n=====RELAZIONE ETA', DURATA ABBONAMENTO, TARIFFA MENSILE, CHURN=====\n")
relation = df.groupby(["Età", "Durata_Abonnamento", "Tariffa_Mensile"])["Churn"].mean()
print(relation)

#correlazioni tra variabili corr()
print("\n=====CORRELAZIONE TRA VARIABILI=====\n")
corr = numbers.corr()
print(corr)

#normalizzazione
print("\n=====NORMALIZZAZIONE=====\n")
df[numbers.columns] = (numbers - numbers.mean()) / numbers.std()
print(df)