import pytest
import sqlite3

@pytest.fixture

def db_connection():
    """"
    Fixture que configura uma conexão com um banco de dados SQLite temporário e garante
    a limpeza dos recursos após o teste
    """
    conn=sqlite3.connect(":memory:") #Cria o banco de dados em memória
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE users(
                   id INTEGER PRIMARY KEY, 
                   name TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE
                   )
        """
    )
    conn.commit()
    yield conn, cursor
    conn.close()

def test_database_insert(db_connection):
   """ Testa a inserção de um usuário na tabela users do BD sqlite """  
   conn, cursor = db_connection
   cursor.execute(""" 
    INSERT INTO users (name, email)
    VALUES (?, ?)
 """, ("Renato Miranda Setúbal","remiset@gmail.com"))
   #verificando a inserção
   cursor.execute("SELECT * from users")
   user = cursor.fetchone()
   assert user is not None
   assert user[1]=="Renato Miranda Setúbal"
   assert user[2]=="remiset@gmail.com"

def test_database_no_duplicate_emails(db_connection):
    """ 
    Testa a inserção de usuários com e-mail já cadastrado
    """
    conn, cursor = db_connection
    cursor.execute(""" 
       INSERT INTO users(name,email)
       VALUES (?, ?)
       """, ("James", "james@gmail.com"))
    conn.commit()
    #    Verificação de tentativa de e-mail duplicado
    with pytest.raises(sqlite3.IntegrityError):
       cursor.execute("""
       INSERT INTO users(name, email)
       VALUES (?, ?)
       """, ("Joao", "james@gmail.com"))
       conn.commit()