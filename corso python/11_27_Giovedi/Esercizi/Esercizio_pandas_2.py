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
#restituisce il valore prodotto corrispondente al valore massimo di quantita
max_sell_id = max_sell.idxmax()
max_quantity = max_sell.max()
print(max_sell_id, max_quantity)

#città con maggiori vendite totali
print("\n=====CITTA' CON MAGGIORI VENDITE TOTALI=====\n")
max_sell_city = df.groupby("Città")["Totale vendite"].sum()
max_sell_id_city = max_sell_city.idxmax()
max_tot_city = max_sell_city.max()
print(max_sell_id_city, max_tot_city)

#dataframe con vendite superiori ad un valore
print("\n=====VENDITE FILTRATE=====\n")
df_2 = df[df["Totale vendite"]>5000]
print(df_2)

#ordinare colonne totale vendite in ordine decrescente
print("\n=====COLONNE TOTALE VENDITE IN ORDINE DECRESCENTE=====\n")
df = df.sort_values(by="Totale vendite", ascending=False)
print(df)

#visualizzare totali vendite per ogni città
print("\n=====TOTALE VENDITE PER OGNI CITTA'=====\n")
tot_city = df.groupby("Città")["Totale vendite"].sum()
print(tot_city)