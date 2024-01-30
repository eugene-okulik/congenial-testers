import pytest
import sys
import allure


@allure.feature('My testing')
@allure.story('first')
def test_me1(text):
    print(text)
    assert 1 == 1


@allure.story('first')
@allure.feature('My testing')
@pytest.mark.skipif(sys.platform == 'linux', reason='not for linux')
def test_me3():
    assert 3 == 3


@allure.story('first')
@allure.feature('My testing')
@pytest.mark.smoke
def test_me4():
    assert 4 == 4


@allure.story('second')
@allure.feature('My testing')
@pytest.mark.regression
def test_me5():
    assert 5 == 5


@allure.story('second')
@allure.feature('My testing')
@pytest.mark.summer
def test_me6():
    assert 6 == 6


@allure.story('second')
@allure.feature('My testing')
@pytest.mark.parametrize('num', [6, 7, 8])
def test_me7(num):
    # assert 7 == num
    assert num == num


@allure.story('successful login')
@allure.feature('Login')
@pytest.mark.parametrize('creds', [('admin', 'password11'), ('user1', 'skdjfhsdjf')])
def test_login(creds):
    login, passw = creds
    print(login, passw)


@allure.feature('My testing')
@allure.story('first')
def test_me11(text):
    print(text)
    assert 1 == 1


@allure.story('first')
@allure.feature('My testing')
@pytest.mark.skipif(sys.platform == 'linux', reason='not for linux')
def test_me31():
    assert 3 == 3


@allure.story('first')
@allure.feature('My testing')
@pytest.mark.smoke
def test_me41():
    assert 4 == 4
