import pytest


@pytest.fixture()
def text(text2):
    return text2 + 'here'


def test_me2(text, text2):
    print(text, text2)
    assert 2 == 2
