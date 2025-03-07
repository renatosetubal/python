import pytest

@pytest.fixture
def list_sample():
    return [10,9,8,7,6]

def test_sum(list_sample):
    assert sum(list_sample) == 40

def test_len(list_sample):
    assert len(list_sample) == 5
