import pytest
"""
On application of the decoration the trailing method get converted into fixture
"""
@pytest.fixture(scope="class")
def oneTimeSetup(browser,osType):

    print ("\nExecute one time setup before starting any test")
    if browser == "firefox":
        print ("\nRuning test in firefox")
    else:
        print ("\nRunning test in othere browser")
    yield
    print ("\nExecute one time tear down after execution of whole test")

# https://docs.pytest.org/en/latest/writing_plugins.html
# https://docs.pytest.org/en/latest/writing_plugins.html#writinghooks
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

