def is_positivo(number):
    return number > 0

def sub(a,b):
    return a -b

def length(list):
    return len(list)

def is_email(email):
    return '@' in email and '.' in email

def somar_lista(valores):
    """Soma todos os valores em uma lista."""
    if not all(isinstance(i,(int,float)) for i in valores):
        raise ValueError("Todos os valores devem ser números")
    return sum(valores)

def encontrar_valor(dicionario, chave):
    """" Encontrar valores dentro de um dicionario baseado na chave passada"""
    if not isinstance(dicionario,dict):
        raise ValueError("O primeiro argumento deve ser um dicionário")
    return dicionario.get(chave, None)