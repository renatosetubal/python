import sqlite3

conexao = sqlite3.connect('bd/filmes.db')
cursor = conexao.cursor()

id=1
cursor.execute("""
        UPDATE filmes SET titulo = ?
        WHERE id = ?
    """, ("007 Gold Eye",id)
)
conexao.commit()
conexao.close()