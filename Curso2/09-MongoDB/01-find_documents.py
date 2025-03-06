import connection as conn
import requests

cliente = conn.retorna_conexao()
db=cliente['nobel']

prizes=db['prizes']
laureates=db['laureates']

#contar documentos por gênero.
print(db.laureates.count_documents({'gender':'female'})) 
print(db.laureates.count_documents({'gender':'male'})) 

#Contar documentos pela diedCountry

print(db.laureates.count_documents({'diedCountry':'France'})) 

#Filtro composto
filter_doc= {
    'diedCountry': 'France',
    'gender': 'female',
    'bornCity' : 'Warsaw'
}

print(db.laureates.count_documents(filter_doc)) 
print(db.laureates.find_one(filter_doc)) 

#Utilizando operador IN
print(db.laureates.count_documents(
    {
        'diedCountry': {
            '$in': ['France','USA']
        }
    }
)) 

#Utilizando operador NE

print(db.laureates.count_documents(
    {
        'diedCountry': {
            '$ne': ['France','USA']
        }
    }
)) 