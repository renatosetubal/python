import sqlite3

conn = sqlite3.connect('bd/filmes.db')
cursor = conn.cursor()

#2- Inserindo dados
cursor.execute("""
    INSERT INTO filmes (titulo, ano, nota)  
    VALUES ('Bad Boys', 1997, 9.5)
"""
)
conn.commit()
conn.close()