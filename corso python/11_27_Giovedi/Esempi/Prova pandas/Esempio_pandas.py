import pandas as pd
import numpy as np

#percorso del file csv
file_path = "corso python/11_27_Giovedi/Esempi/Prova pandas/vendite.csv"

#caricamento dei dati nel dataframe
df = pd.read_csv(file_path)

#le prime righe del dataframe per confermare
print(df.head())

#dataFrame esempio, inclusi valori mancanti e duplicati
data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
    'Età': [25, 30, 22, 30, np.nan, 25, 29],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
}

df = pd.DataFrame(data)

#stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

#selezione delle righe dove l'età è superiore a 23, creando una copia del dataframe
df_older = df[df['Età'] > 23]

#stampa delle righe selezionate
print("\nPersone con età superiore a 23 anni:")
print(df_older)

#aggiungiamo una nuova colonna  la persona maggiorenne
df['Maggiorenne'] = df['Età'] >= 18

#stampa del DataFrame con la nuova colonna
print("\nDataFrame con colonna 'Maggiorenne':")
print(df)

#rimozione dei duplicati
df = df.drop_duplicates()

#gestione dei dati mancanti
#rimozione delle righe dove almeno un elemento è mancante
df_cleaned = df.dropna()

#possiamo sostituire dati mancanti con valore di default
#inplace modifica il dataset se impostato su True, conviene metterlo a False prima di modificare per vedere i dati come sono stati modificati
df['Età'].fillna(df['Età'].mean(), inplace=True)

#stampa del DataFrame pulito

print("\nDataFrame dopo la pulizia:")
print(df_cleaned)

#stampa del DataFrame con dati mancanti sostituiti
print("\nDataFrame con dati mancanti sostituiti:")
print(df)

#aggiungiamo una nuova colonna  la persona maggiorenne
df['Maggiorenne'] = df['Età'] >= 18

#stampa del DataFrame con la nuova colonna
print("\nDataFrame con colonna 'Maggiorenne' dopo la sostituizione:")
print(df)

#stampa del DataFrame originale
print("DataFrame Originale:")
print(df)