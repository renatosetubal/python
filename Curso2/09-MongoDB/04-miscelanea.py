import connection as conn

cliente = conn.retorna_conexao()
db=cliente['nobel']

pr=db['prizes']
laureates=db['laureates']

""" Toldos os laureaveis que possuem prêmio
 em física e que seja compartilhado"""
consulta = db.laureates.count_documents(
    {
        'prizes' :{
            '$elemMatch':{
                'category':'physics',
                'share': '1'
            }
        }
    }
)
print(consulta)

""" Toldos os laureaveis que possuem prêmio
 em física anterior 1945 """
consulta2 = db.laureates.count_documents(
    {
        'prizes' :{
            '$elemMatch':{
                'category':'physics',
                'share': '1',
                'year':{'$lt':'1945'}
            }
        }
    }
)
print(consulta2)

"""Utilizando regex 
   Traz alguns laureados que nasceram em lugares que se tornaram Polônia"""
   
consulta3 = db.laureates.distinct(
        'bornCountry',
        {'bornCountry': {'$regex':'Poland'}}
)
print(consulta3)

"""Utilizando regex 
   case insensitive"""
consulta4 = db.laureates.distinct(
        'bornCountry',
        {'bornCountry': {'$regex':'Poland', '$options':"i"}}
)
print(consulta4)


"""Utilizando classe """
from bson.regex import Regex
consulta5 = db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('poland','i')}
)
print(consulta5)

"""Começa com P"""
consulta6=db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('^Poland')}
)
print(consulta6)

"""Termina com \ escape parêmtesos"""
consulta7=db.laureates.distinct(
    'bornCountry',
    {'bornCountry': Regex('now Poland\)')}
)
print(consulta7)
