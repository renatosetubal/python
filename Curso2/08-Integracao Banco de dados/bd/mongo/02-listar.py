import connection as conn
from pprint import pprint

cliente = conn.retorna_conexao()
db = cliente.dbposts
col = db.posts

result = col.find()
for r in result:
    pprint(r)