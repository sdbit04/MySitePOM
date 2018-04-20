from Include.PytestFrameWorkApproch.BasePkg.DriverClassModule import DriverCreator
from Include.PytestFrameWorkApproch.PagePkg.LoginPage import LoginPage
import unittest
Browser="FireFox"
# Try to use fixture at here
LoginPageOB=LoginPage(Browser)
class LoginTestClass(unittest.TestCase):
    #We have inheritade the unittest.TestCase class to allow all the methodes into class prefix test_ will get executed by py.test
    #If we dont do this, then py.test will report that, there is no test cases to be executed
    # def test_login(self):
    #     Driver.get(BaseUrl)
    #     LoginPageob = LoginPage(Driver)
    #     LoginPageob.clickToLoginLink()

    def test_invalidLogin(self):
        LoginPageOB.invalidLogin('sdbit04@gmail.com', 'abcd')
        # Element, TorF=LoginPageOB.getElementWithResult('xpath', "//div[contains(text(), 'Invalid email or password')]")
        Element, TorF=LoginPageOB.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        assert TorF == True

"""
LoginPageOB=LoginPage("FireFox")
LoginPageOB.Driver.get(LoginPageOB._baseUrl)
LoginPageOB.clickLogin()
LoginPageOB.sendUserId('sdbit04@gmail.com')
LoginPageOB.sendPassword('avdcd')
LoginPageOB.clickSubmit()
time.sleep(10)
LoginPageOB.Driver.close()
"""
