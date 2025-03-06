import connection as conn

cliente = conn.retorna_conexao()
db=cliente['nobel']

pr=db['prizes']
laureates=db['laureates']

# 1 - valor incluído
# 2 - valor não incluído

docs = db.laureates.find(
    filter = {},
    projection = {
        'prizes.affiliations': 1,
        '_id': 0
    }
)
print(list(docs[:3]))

#Projecao com campos ausentes
docs2 = db.laureates.find(
    filter = {'gender': 'org'},
    projection = ['bornCountry', 'firstname']
)
print('\n')
print(list(docs2[:3]))