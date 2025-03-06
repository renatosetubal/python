import connection as conn
from pprint import pprint

cliente = conn.retorna_conexao()
db = cliente.dbposts
col = db.posts

query={"title": "FastAPi"}

x=col.delete_one(query)
print(x.deleted_count, " documents deleted.")