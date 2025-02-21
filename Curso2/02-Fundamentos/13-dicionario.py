filme = {
    "title": "Carmagedoom",
    "ano": 1989,
    "aval": 9.2,
    "genero": ['Terror','Ação','Drama']
}
print(filme)
#Recuperar um elemento de um dicionario
print(filme['genero'])
print(filme.get("title"))
# Mostrar apenas as chaves do dicionario
print(filme.keys())
# Buscar apenas os valores do dicionario
print(filme.values())
# Buscar item do dicionario com chave  e valor
print(filme.items())
#Adicionar item ao dicionario
filme['Ator'] = "The rock"
print(filme.items())
#Atualizar um valor no dicionario
filme.update({"ano":2020})
print(filme.items())
#Remover um item do dicionario

filme.pop("genero")
print(filme.items())
