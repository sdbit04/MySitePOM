import pytest
@pytest.fixture()
def SetUpFixture():
    print ("\nRun at the begining of each steps")
    yield
    print ("\nRun at the end of each test steps")

@pytest.fixture(scope="module")
def SetUpOneTimeModuleFixture():
    print ("\nRun at the begining of whole test *****t")
    yield
    print ("\nRun at the end of whole test ******")

@pytest.fixture(scope="class")
def SetUpOneTimeClassFixture():
    print ("\nRun at the begining of whole test *****t")
    yield
    print ("\nRun at the end of whole test ******")

