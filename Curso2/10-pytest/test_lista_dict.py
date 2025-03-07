from functions import somar_lista,encontrar_valor
import pytest

def test_somar_lista():
    assert somar_lista([1,2,3]) == 6
    assert somar_lista([10.5,4.5,5]) == 20
    assert somar_lista([]) == 0
    with pytest.raises(ValueError):
        somar_lista([1,2,'renato'])

def test_encontrar_valor():
    dict={'a':1,'b':2,'c':5}
    assert encontrar_valor(dict,'c') == 5   
    assert encontrar_valor(dict,'a') == 1 
    assert encontrar_valor(dict,'b') == 2     
    assert encontrar_valor(dict,'d') == None  
    
    with pytest.raises(ValueError):
        encontrar_valor("Não é um dicionário",'a')
