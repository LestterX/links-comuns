import sqlite3 as sq

def get_deb_connection():
    conn = sq.connect('static/db/database.db')
    return conn

def verificar_nome_db(user):
    conn = get_deb_connection()
    nomes = conn.execute('SELECT nome FROM sites ORDER BY nome ASC').fetchall()
    count = 0
    for nome in nomes:
        if nome[0] == user:
            print("Tem")
        else:
            print("Não tem")
            count = count + 1
            continue
        count = count + 1

verificar_nome_db('Celpe')