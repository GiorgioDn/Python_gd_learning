import pandas as pd
import numpy as np

prodotti = [ "Computer", "Portatile", "Tablet"]
citta = [ "Bologna", "Torino", "Roma"]

size_data = 21

#creazione del dataframe casuale
df = pd.DataFrame({
    "Prodotto": np.random.choice(prodotti, size_data),
    "Data": np.random.randint(1, 31, size_data),
    "Città": np.random.choice(citta, size_data),
    "Vendite": np.random.randint(0, 11, size_data),
})

print("\n=====TABELLA INIZIALE=====\n")
print(df)

#tabella pivot vendite medie
print("\n=====PIVOT VENDITE MEDIE=====\n")
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean', fill_value=0).reset_index()
print(pivot_df)

#tabella groupby vendite totali
print("\n=====GROUPBY VENDITE TOTALI=====\n")
tot_sell = df.groupby("Prodotto")["Vendite"].sum().reset_index()
print(f"{tot_sell}\n")