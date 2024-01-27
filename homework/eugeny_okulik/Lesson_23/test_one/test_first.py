import pytest
import sys


def test_me1(text):
    print(text)
    assert 1 == 1


@pytest.mark.skipif(sys.platform == 'linux', reason='not for linux')
def test_me3():
    assert 3 == 3


@pytest.mark.smoke
def test_me4():
    assert 4 == 4


@pytest.mark.regression
def test_me5():
    assert 5 == 5


@pytest.mark.summer
def test_me6():
    assert 6 == 6


@pytest.mark.parametrize('num', [6, 7, 8])
def test_me7(num):
    assert 7 == num


@pytest.mark.parametrize('creds', [('admin', 'password11'), ('user1', 'skdjfhsdjf')])
def test_login(creds):
    login, passw = creds
    print(login, passw)
