import sqlite3
import os

# Nome del file database
db_filename = 'corso python/11_26_Mercoledi/Esempi/db_example/libreria_esempio.db'

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

# 4. INSERIMENTO DATI (INSERT) - Metodo Singolo
# NOTA: Uso '?' come placeholder per sicurezza (evita SQL Injection)
sql_insert = "INSERT INTO libri (titolo, autore, anno, prezzo) VALUES (?, ?, ?, ?)"
dati_libro = ("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 25.50)

cursor.execute(sql_insert, dati_libro)
print("Inserito un singolo libro.")
#invia le modifiche
conn.commit()

# 5. INSERIMENTO MULTIPLO (executemany) - Molto più veloce per tanti dati
lista_libri = [
    ("1984", "George Orwell", 1949, 12.00),
    ("Il Piccolo Principe", "Antoine de Saint-Exupéry", 1943, 9.50),
    ("Dune", "Frank Herbert", 1965, 18.90),
    ("Python Crash Course", "Eric Matthes", 2019, 35.00)
]

cursor.executemany(sql_insert, lista_libri)
print(f"Inseriti {cursor.rowcount} libri in blocco.")

# 6. SALVATAGGIO (COMMIT)
# Fondamentale! Senza questo, i dati verrebbero persi alla chiusura.
conn.commit()
print("Modifiche committate (salvate) nel DB.")

# 7. LETTURA DATI (SELECT)
print("\n--- Lettura di tutti i libri ---")
cursor.execute("SELECT * FROM libri")

# fetchall() recupera tutte le righe rimanenti come una lista di tuple
tutti_i_libri = cursor.fetchall()

for libro in tutti_i_libri:
# libro è una tupla: (id, titolo, autore, anno, prezzo)
    print(f"ID: {libro[0]} | Titolo: {libro[1]} | Prezzo: {libro[4]}€")