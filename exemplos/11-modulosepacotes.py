################listar módulos instalados
#py -m pip list
################Instalar módulo matplotlib e suas dependencias
#py -m pip install matplotlib
################Trazer informação do pacote
#py -m pip show matplotlib
################


#from math import * -> import universal de todas as funções
#import math #Importando o modulo. 
from math import sqrt,sinh
import math as m #importanto o modulo com apelido. 
#print(math.sqrt(81))

#Importando modulo criado na mesma pasta modulo.py
import modules as m

if __name__ == '__main__': #serve para impedir emissão de comandos antes da hora. 
    m.msg1()