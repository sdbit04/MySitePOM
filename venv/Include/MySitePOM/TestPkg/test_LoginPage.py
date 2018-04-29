from Include.MySitePOM.BasePkg.DriverClassModule import DriverCreator
from Include.MySitePOM.PagePkg.LoginPage import LoginPage
import unittest
import pytest
Browser="FirefoX"
@pytest.fixture()
def testSetup():
    LoginPageOB = LoginPage(Browser)
    print("Setting up data")
    return LoginPageOB

# Try to use fixture at here
# LoginPageOB=LoginPage(Browser)
class TestLoginClass():
    #We have inheritade the unittest.TestCase class to allow all the methodes into class prefix test_ will get executed by py.test
    #If we dont do this, then py.test will report that, there is no test cases to be executed
    # def test_login(self):
    #     Driver.get(BaseUrl)
    #     LoginPageob = LoginPage(Driver)
    #     LoginPageob.clickToLoginLink()

    def test_invalidLogin(self, testSetup):
        # LoginPageOB.invalidLogin('sdbit04@gmail.com', 'abcd')
        testSetup.invalidLogin('sdbit04@gmail.com', 'abcd')
        # Element, TorF=LoginPageOB.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        Element, TorF=testSetup.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        assert TorF == True
