

from PagePkg.LoginPage import LoginPage
import pytest
Browser = "Firefox"
"""
One way to use create fixture with scope=method, default level of scope
@pytest.fixture()
def testSetup():
    LoginPageOB = LoginPage(Browser)
    print("Setting up data")
    return LoginPageOB
"""


@pytest.fixture(scope="class")
def testSetup():
    print("creating object of PageClass using fixture")
    LoginPageOB = LoginPage(Browser)
    return LoginPageOB

@pytest.fixture(scope="class")
def onetimeSetup():
    print("Preparing data setup")
