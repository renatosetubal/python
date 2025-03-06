import sqlite3
#Conectando ao banco de dados   
conexao = sqlite3.connect('bd/filmes.db')

#Criando cursor
cursor = conexao.cursor()

#Criando tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    ano INTEGER NOT NULL,
    nota REAL NOT NULL
);
''')
conexao.close()
