import pytest


def test_def1():
    assert 1 == 1


def test_invalidLogin(testSetup):
    testSetup.invalidLogin('sdbit04@gmail.com', 'abcd')
    Element, TorF=testSetup.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
    assert TorF == True


def test_def2():
    assert 3 == 3
