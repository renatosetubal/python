from pymongo import MongoClient

def retorna_conexao():
    client = MongoClient(
    host='localhost',
    port=27017,
    username='admin',          
    password='P@ssw0rd',     
    authSource='admin')
    return client