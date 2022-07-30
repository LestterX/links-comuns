from multiprocessing import connection
import sqlite3 as sq

connection = sq.connect('database.db')

with open("schema.sql") as f: #schema.sql
    connection.executescript(f.read())

cursor = connection.cursor()

# cursor.execute("INSERT INTO sites (nome, link) VALUES ('asdw', 'https://www.detran.pe.gov.br/')")

connection.commit()
connection.close()