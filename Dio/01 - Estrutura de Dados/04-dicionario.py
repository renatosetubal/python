#criando um dicionário de dados Dict. 
contatos = {
    "remiset@gmail.com": {"nome":"Renato", "telefone":"999108139","idade":42},
    "luana.lins2@gmail.com": {"nome":"Luana", "telefone":"999237989","idade":38},
    "jose@gmail.com": {"nome":"Jose das Couves", "telefone":"9999999","idade":90,"obs":{"detalhes":"Eu sou um ancião"}} #inclusão de dados dentro de dados. 

}

# print(contatos["luana.lins2@gmail.com"]["idade"])
# print(contatos["remiset@gmail.com"]["nome"])
# print(contatos["jose@gmail.com"]["obs"]["detalhes"])

#For para percorrer o dicionário de dados

for chave, valor in contatos.items():
    print(f'{chave} - {valor}')

#Copia de dicionario
copia = contatos.copy()

#print(copia["jose@gmail.com"]["nome"])

#Usando keys
user={"id01":{"nome":"Renato Miranda","telefone":"9999999"}}
result = user.keys() #Vai retornar as chaves de um dicionário. 
print(result)

