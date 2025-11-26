import sqlite3

#connessione al database
conn = sqlite3.connect('esempio.db')
cur = conn.cursor()

#query con filtro
cur.execute("SELECT nome, voto FROM studenti WHERE voto > ?", (25, ))

#recupero risultati
studenti_meritevoli = cur.fetchall()

#stampa dei risultati
for nome, voto in studenti_meritevoli:
    print(f"{nome} ha preso {voto}")
    
#chiusura connessione
conn.close()

