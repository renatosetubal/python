import sqlite3

conexao = sqlite3.connect('bd/filmes.db')
cursor = conexao.cursor()
id = (1,2)
cursor.execute("""
    DELETE FROM filmes WHERE id in (?,?)
""", id
)
conexao.commit()
conexao.close()