import xml.etree.ElementTree as et

dados = """<?xml version="1.0" encoding='utf-8'?>
<clientes>
    <cliente>
        <id>1</id>
        <nome>Hugo</nome>
        <idade>35</idade>
        <cidade>Curitiba</cidade>
    </cliente>
     <cliente>
        <id>2</id>
        <nome>Renato</nome>
        <idade>44</idade>
        <cidade>Vila Velha</cidade>
    </cliente>
</clientes>
"""
path = 'dados/clientes.xml'

with open(path, 'w', encoding='utf-8') as f:
    f.write(dados)

#Lendo dados
tree = et.parse(path)
root = tree.getroot()
for c in root.findall('cliente'):
    id = c.find('id').text
    nome = c.find('nome').text
    idade = c.find('idade').text
    cidade = c.find('cidade').text
    print(f'ID: {id}, Nome: {nome}, Idade: {idade}, Cidade: {cidade}')

#Adicionando um novo cliente
cliente = et.Element('cliente')
id = et.SubElement(cliente, 'id')
id.text = '3'
nome = et.SubElement(cliente, 'nome')  
nome.text = 'Maria'
idade = et.SubElement(cliente, 'idade')
idade.text = '30'
cidade = et.SubElement(cliente, 'cidade')
cidade.text = 'São Paulo'
root.append(cliente)
tree.write(path,encoding='utf-8',xml_declaration=True)