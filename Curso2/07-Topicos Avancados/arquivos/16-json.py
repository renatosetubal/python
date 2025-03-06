import json

# Dicionário   
dicionario = {
    "clientes": [
        {
            "nome": "João",
            "idade": 25,
            "cidade": "São Paulo",
            "estado": "SP"
        },
        {
            "nome": "Maria",
            "idade": 30,
            "cidade": "Rio de Janeiro",
            "estado": "RJ"
        }
    ]
}

path_arquivo="clientes.json"

#1-Escrevendo um arquivo JSON
with open(path_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(dicionario, arquivo, indent=4)

#2-Lendo um arquivo JSON
with open(path_arquivo, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    print(dados)
    print(dados["clientes"][0]["nome"])

#3-Manipulando um arquivo JSON
for cliente in dados["clientes"]:
   if cliente["nome"] == "João":
      cliente["idade"] = 20
      break
novo={"id":3,"nome":"Pedro","idade":35,"cidade":"Belo Horizonte","estado":"MG"}
dados["clientes"].append(novo)

#4-Atualizando um arquivo JSON
with open(path_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)