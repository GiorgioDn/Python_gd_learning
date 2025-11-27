import pandas as pd
import numpy as np

#lista generata da chat gpt
nomi = [ "Lorenzo", None, "Giulia", "Martina", "Alessio", "Sara", None, "Davide", "Chiara", "Michele", "Elena" ]
citta = [ "Bologna", "Torino", None, "Firenze", "Napoli", None, "Genova", "Perugia" ]

size_data = 31

#creazione del dataframe casuale
df = pd.DataFrame({
    "Nome": np.random.choice(nomi, size_data),
    "Età": np.random.randint(14, 61, size_data),
    "Città": np.random.choice(citta, size_data),
    "Salario": np.random.randint(1600, 3600, size_data),
})

#indice nan per i l'età ed il salario
for col in ["Età", "Salario"]:
    indici_nan = np.random.choice(df.index, size=3, replace=False)
    df.loc[indici_nan, col] = np.nan

#filtro colonne numeriche
numbers = df.select_dtypes(include=["float64", "int64"])

print(df)

#creo la copia per modifiche del dataframe
df_copy = df.copy()

#visualizzazione prime 5 righe
print("\n=====PRIME 5 RIGHE=====\n")
print(df.head())

#visualizzazione ultime 5 righe
print("\n=====ULTIME 5 RIGHE=====\n")
print(df.tail())

#calcolo statistiche descrittive
print("\n=====STATISTICHE DESCRITTIVE=====\n")
stats = df.describe()
print(stats)

#rimozione duplicati
print("\n=====RIMOZIONE DUPLICATI=====\n")
df_copy = df.drop_duplicates()
print(df_copy)

#valori mancanti sostituiti con la mediana
print("\n=====SOSTITUIZIONE VALORI MANCANTI=====\n")
for col in numbers.columns:
    median = df_copy[col].median()
    df_copy[col] = df_copy[col].fillna(median)
    
print(df_copy)

#rimozione valori mancanti
print("\n=====RIMOZIONE VALORI MANCANTI=====\n")
df_copy = df_copy.dropna()
print(df_copy)

#aggiungiamo una nuova colonna la persona maggiorenne
print("\n=====AGGIUNTA DI UNA COLONNA=====\n")
def classifica_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 45:
        return "Adulto"
    else:
        return "Senior"

df_copy["Categoria Età"] = df_copy["Età"].apply(classifica_eta)
print(df_copy)

#salvataggio del dataframe su csv
file_path = "corso python/11_27_Giovedi/Esercizi/dataset/work.csv"
df_copy.to_csv(file_path)

