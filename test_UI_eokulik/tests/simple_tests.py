import pytest


@pytest.mark.simple
def test_one():
    assert 1 == 1


@pytest.mark.simple
def test_two():
    assert 1 == 1


@pytest.mark.simple
def test_three():
    assert 1 == 1
