import psycopg2 as pg2

conn = pg2.connect(
    database='games',
    user = 'postgres',
    password = 'P@ssw0rd',
    host = '192.168.0.111',
    port = '5432'
)