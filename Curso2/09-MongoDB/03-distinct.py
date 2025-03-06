import connection as conn

cliente = conn.retorna_conexao()
db=cliente['nobel']

pr=db['prizes']
laureates=db['laureates']

#Lista o mapeamento de generos
#Agregação processar os dados em uma coleção
#e produzir o resultado que foi gerado

print(db.laureates.distinct('gender'))
print(db.laureates.count_documents({'gender':'female'}))
print(db.laureates.count_documents({'gender':'male'}))
print(db.laureates.count_documents({'gender':'org'}))

#Lista o mapeamento de categoria dos premios a partir do laureates
print(db.laureates.distinct('prizes.category'))

#Alguns premios que foram compartilhados
#Quais categorias do premio, alem de fisica
#tem laureado com acoes trimestrais?
print(db.laureates.distinct(
    'prizes.category',
    {'prizes.share':"4"}
))
print(db.prizes.distinct(
    'category',
    {'laureates.share':"4"}
))

"""
Categoria que ganhou mais de um premio
"""
print(db.laureates.distinct(
    'prizes.category',
    {'prizes.1':{
        '$exists':True
    }}
))
