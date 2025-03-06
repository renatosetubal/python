import connection as conn
import timeit

cliente = conn.retorna_conexao()
db=cliente['nobel']
prizes=db['prizes']
laureates=db['laureates']

#1-Todos os premios compartilhados entre 3 pessoas

for doc in db.prizes.find({
    'laureates.share':'3'}):
    print('{year} {category}'.format(**doc))
    
    print('\n')
#2- Limitar em 5 registros
for doc in db.prizes.find({
    'laureates.share':'3'}, limit=5):
    print('{year} {category}'.format(**doc))

#3 - Pulando os 10 primeiros resultados
print('Pulando os 10 primeiros registros. \n')
for doc in db.prizes.find({
    'laureates.share':'3'}, skip=10, limit=5):
    print('{year} {category}'.format(**doc))
print('\n')
print('Refatorando e reodenando')
#4 - Refatorando | ordenando ascendentemente
for doc in db.prizes.find({'laureates.share':'3'}) \
    .sort([('year',1)]) \
    .skip(3) \
    .limit(3):
        print('{year} {category}'.format(**doc))