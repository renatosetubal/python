from functions import is_positivo

def test_soma():
    assert sum([1,2,7]) == 10


def  teste_positivo():
    assert is_positivo(5) is True
    assert is_positivo(-1) is False