import re
#
text = "Udemy uma plataforma com muitos cursos!"
match=re.search(r'muitos cursos',text) #r significa raw string, string bruta
print(f'Posicao inicial: {match.start()}') #indice inicial
print(f'Posicao inicial: {match.end()}') #Indice final

#Buscando o indice que possui o ponto
site='https://udemy.com'
match = re.search(r'\.',site)
print(match)

#Buscando uma lista de caractere dentro de uma frase

pattern = "[g-m]"
result = re.findall(pattern,text)
print(result)

#4 - Inicio de uma string

rule = r'^A'
frases = ['A casa está suja',"O dia está lindo","Eu estou com sono","A sogra é benção"]
for f in frases:
    if re.match(rule,f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não Corresponde: {f}')

#5 Verificar o final de uma string
rule=r'!$'
frase2="O dia está lindo!"
match = re.search(rule,frase2)
if match:
    print(f'Sim corresponde!')
else:
    print(f'Não corresponde!')

        
