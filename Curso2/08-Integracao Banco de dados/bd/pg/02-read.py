from conexao import conn

cursor = conn.cursor()

def lista_jogos(cursor):
    cursor.execute('SELECT * FROM games')
    result=cursor.fetchall()
    for res in result:
        print(res)
       
lista_jogos(cursor)
conn.close()