import connection as conn
import requests

cliente = conn.retorna_conexao()
db = cliente['nobel']

for collection_name in ["prizes", "laureates"]:
    response = requests.get(
        f"http://api.nobelprize.org/v1/{collection_name[:-1]}.json",
        verify=False  # Ignora a validação SSL
        )
    documents=response.json()[collection_name]
    db[collection_name].insert_many(documents)
    
prizes = db["prizes"]
laureates = db["laureates"]
len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})
print(f"Prizes: {len_prizes}")
print(f"Laureates: {len_laureates}")