import sqlite3

conexao = sqlite3.connect('bd/filmes.db')
cursor = conexao.cursor()

#3- Lendo dados
cursor.execute('SELECT * FROM filmes')
for linha in cursor.fetchall():
    print(linha[1])