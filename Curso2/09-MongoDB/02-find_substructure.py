import connection as conn

cliente = conn.retorna_conexao()
db=cliente['nobel']

prizes=db['prizes']
laureates=db['laureates']

#Buscando o primeiro documento
user = db.laureates.find_one(
    {
        'firstname': 'Hendrik A.',
        'surname' : 'Lorentz'
        
    }
)
print(user)

#Pesquisando em uma subestrutura

faculdade = db.laureates.count_documents({
    'prizes.affiliations.name':'University of California'
})
print(faculdade)
sanFrancisco = db.laureates.count_documents({
    'prizes.affiliations.city':'San Francisco, CA'
})
print(f'Quantidade de Laureados na cidade de São Francisco: {sanFrancisco}')

#Conta documentos que não possua uma informação. 
no_country = db.laureates.count_documents({
        'bornCountry':{
            '$exists': False
        }
    })
print(f'Quantidade de documentos sem país de nascimento: {no_country}')

#Verificar se laureados possuem premios
qtd_prizes = db.laureates.count_documents({
    'prizes':{
        '$exists': True
    }
})
print(f'Quantidade de laureados que possuem prêmios: {qtd_prizes}')

#Verificação se o prize está preenchido
prize_contain = db.laureates.count_documents({
    'prizes.0':{
        '$exists': True
    }
})
print(f'Quantidade de prizes: {prize_contain}')

#Verificar quem tem mais de um premio
prize_multi = db.laureates.count_documents({
    'prizes.1':{
        '$exists': True
    }
})
print(f'Quantidade de laureados com mais de um prêmio : {prize_multi}')


