from conexao import conn

cursor = conn.cursor()

sql = """
    UPDATE games
    SET name = %s
    WHERE id = %s
"""
cursor.execute(sql, ('Zelda', 1))
conn.commit()
print('Registro atualizado com sucesso!')
conn.close()