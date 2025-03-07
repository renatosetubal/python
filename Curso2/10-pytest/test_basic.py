from functions import sub,length,is_email

def test_sub_len():
    assert sub(3,2) == 1
    assert length([1,2,3,4]) == 4

def test_email():
    assert is_email('remiset@gmail.com') is True
    assert is_email('joao.com') is False
    assert is_email('joao@com') is False

