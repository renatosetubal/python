import connection as conn

cliente = conn.retorna_conexao()
db=cliente['nobel']

prizes=db['prizes']
laureates=db['laureates']

#Ordenacao ascendente
cursor = db.prizes.find(
    {'category':'physics'},
    ['year'],
    sort=[('year',1)] #1 acendente, -1 ascendente
)

print([doc['year'] for doc in cursor][:5])

#Descendente
cursor2 = db.prizes.find(
    {'category':'physics'},
    ['year'],
    sort=[('year',-1)] #1 acendente, -1 ascendente
)
print([doc['year'] for doc in cursor2][:5])

#Premios entre 1966 e 1970

for doc in db.prizes.find(
    {'year':{'$gt':'1966', '$lt':'1970'}},
    ['category', 'year'],
    sort=[('year',1), ('category',-1)]):
    print('{year} {category}'.format(**doc))

    