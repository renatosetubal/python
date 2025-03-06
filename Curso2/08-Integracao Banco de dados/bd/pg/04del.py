from conexao import conn

cursor = conn.cursor()

sql = """
    DELETE FROM games
    WHERE id = %s
"""
cursor.execute(sql, (1, ))
conn.commit()
print('Registro deletado com sucesso!')
conn.close()