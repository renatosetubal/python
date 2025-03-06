from conexao import conn


cursor = conn.cursor()
games = [ 
    ('007 Golden Eye', 1998, 8.5),
    ('Mario Kart 3D', 1997, 9.0),  
    ('Super Star Soccer Deluxe', 1996, 10.0),
    ('Fifa 98', 1998, 8.8)
]

def insere_jogo(cursor, games):
    for game in games:
        cursor.execute('INSERT INTO games (name, year, score) VALUES (%s, %s, %s)', game)
        conn.commit()
        print('Games inseridos com sucesso!')
    conn.close()

insere_jogo(cursor, games)




