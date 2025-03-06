import sqlite3

def conecta_bd():
    conn = sqlite3.connect('bd/filmes.db')
    return conn

def add_filme(titulo, ano, nota):
    conn = conecta_bd()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO filmes (titulo, ano, nota) VALUES (?, ?, ?)', (titulo, ano, nota))
    conn.commit()
    conn.close()

def lista_filmes():
    conn = conecta_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM filmes')
    filmes = cursor.fetchall()
    conn.close()
    return filmes
