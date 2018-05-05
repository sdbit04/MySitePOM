import pytest

"""
Here the fixture are applicable for each test methode.
We can use fixer at class level, like it will run once for all the test methodes
We can also use to run fixer for multiple modules
"""
@pytest.mark.run(order=3)
def test_Steps3(SetUpOneTimeModuleFixture, SetUpFixture):
    print ("Running 3rd steps of the test2")

@pytest.mark.run(order=2)
def test_Steps1(SetUpOneModuleTimeFixture, SetUpFixture):
    print("Running first steps of the test2")
@pytest.mark.run(order=1)
def test_Steps2(SetUpOneTimeModuleFixture, SetUpFixture):
    print ("Running 2nd steps of the test2")

