import pytest

"""
Here the fixture are applicable for each test methode.
We can use fixer at class level, like it will run once for all the test methodes
We can also use to run fixer for multiple modules
"""


def test_Steps1(SetUpFixture):
    print("Running first steps of the test1")

def test_Steps2(SetUpFixture):
    print ("Running 2nd steps of the test1")

