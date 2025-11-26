import sqlite3
import os

# Nome del file database
db_filename = 'corso python/11_26_Mercoledi/Esempi/libreria_esempio.db'

# Rimuovo il file se esiste già per avere un ambiente pulito ad ogni esecuzione
if os.path.exists(db_filename):
    os.remove(db_filename)

# 1. CREAZIONE E CONNESSIONE
# Se il file non esiste, viene creato. Se esiste, viene aperto.
print(f"--- Connessione a {db_filename} ---")
conn = sqlite3.connect(db_filename)

# 2. CREAZIONE DEL CURSORE
# Il cursore è il "braccio operativo" della connessione
cursor = conn.cursor()

# 3. CREAZIONE TABELLA (DDL)
# Usiamo le triple quotes per scrivere SQL su più righe in modo pulito
sql_create_table = """
CREATE TABLE IF NOT EXISTS libri (
id INTEGER PRIMARY KEY AUTOINCREMENT,
titolo TEXT NOT NULL,
autore TEXT NOT NULL,
anno INTEGER,
prezzo REAL
);
"""
cursor.execute(sql_create_table)
print("Tabella 'libri' creata con successo.")