import pickle
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'Cliente: {self.nome}, Idade: {self.idade}'

clientes = [
    Cliente('Hugo', 35),
    Cliente('Rose', 25),
    Cliente('João', 18),
    Cliente('Maria', 30)
]

with open('dados/clientes.pkl', 'wb') as f:
    pickle.dump(clientes, f)


#Adicionar novo 
novo_cliente = Cliente('José', 45)
with open('dados/clientes.pkl', 'wb') as f:
    clientes.append(novo_cliente)
    pickle.dump(clientes, f)

#Carregando dado do arquivo
with open('dados/clientes.pkl', 'rb') as f:
    clientes_carregados = pickle.load(f)
    for cliente in clientes_carregados:
        print(cliente)