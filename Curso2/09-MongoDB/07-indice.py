import connection as conn
import timeit

cliente = conn.retorna_conexao()
db=cliente['nobel']
prizes=db['prizes']
laureates=db['laureates']

#Busca premios de 1910
def premios_1910():
    list(db.prizes.find({'year':'1910'}))

def mede_tempo(function):
    tempo=timeit.timeit(function,globals=globals(),
                        number=1) *1000
    print(f'Tempo de execução é de: {tempo:.2f} milisegundos')
    

mede_tempo(premios_1910)
#Criando um indice antes de executar a função
db.prizes.create_index([('year',-1)])
mede_tempo('premios_1910()')

#criando indice composto
db.prizes.create_index([('category',1),('year',1)])
def busca_economia():
    list(db.prizes.find(
        {'category':'economics'},
        {'year':1, '_id':0}))

mede_tempo('busca_economia()')

    