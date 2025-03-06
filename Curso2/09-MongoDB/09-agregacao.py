import connection as conn
import timeit

cliente = conn.retorna_conexao()
db=cliente['nobel']
prizes=db['prizes']
laureates=db['laureates']

cursor=db.laureates.find(
    filter = {'bornCountry':'USA'},
    projection = {'prizes.year':1},
    limit=3    
)
for doc in cursor:
    print(doc['prizes'])
    
#Refatorando consulta com agregações

print('\n')

cursor2=db.laureates.aggregate([
    {'$match':{'bornCountry':'USA'}},
    {'$project': {'prizes.year':1}}, 
    {'$limit':3}   
])

for doc in cursor2:
    print(doc['prizes'])
    
#Adicionando novas etapas na agregação
from collections import OrderedDict
print(list(db.laureates.aggregate([
    {'$match':{'bornCountry':'USA'}},
    {'$project': {'prizes.year':1, '_id':0}}, 
    {'$sort':OrderedDict([('prizes.year',1)])},
    {'$limit':3},
    {'$skip':1}   
])))

#Quantos laureados nascidos nos estados unidos
print(list(db.laureates.aggregate([
    {'$match':{'bornCountry':'USA'}},
    {'$count': 'qtd'}
])))