import connection as conn
from pprint import pprint

cliente = conn.retorna_conexao()
db = cliente.dbposts
col = db.posts

old_value= {'level': 'Intermediário'}
new_value= {'$set': {'level': 'Básico'}}
col.update_one(old_value, new_value)

for x in col.find():
    pprint(x)