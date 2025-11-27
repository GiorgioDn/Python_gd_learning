import pandas as pd

file_path = "vendite.csv"

#creazione del dataset dal file
df = pd.read_csv(file_path)
print(df)

#aggiungo una nuova colonna con il totale delle vendite
print("\n=====AGGIUNTA DI UNA COLONNA=====\n")
df["Totale vendite"] = df["Quantita"] * df ["Prezzo unitario"]
print(df)

#raggruppamento dati prodotto
print("\n=====TOTALE VENDITE PRODOTTO=====\n")
#con groupby ragggruppa le colonne colonne e seleziona la colonna totale vendite di ogni gruppo
#reset_index fa visualizzare l'indice delle righe per una visualizzazione simile al dataframe
result = df.groupby("Prodotto")["Totale vendite"].sum().reset_index()
print(result)

#prodotto più venduto
print("\n=====PRODOTTO CON MAGGIORI VENDITE=====\n")
max_sell = df.groupby("Prodotto")["Quantita"].sum()
max_sell_id = max_sell.idxmax()
max_quantity = max_sell.max()
print(max_sell_id, max_quantity)