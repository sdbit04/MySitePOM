import pytest
"""
#One way of using fixture to create object of class under test

class TestLoginClass:

    def test_invalidLogin(self, testSetup):
        # LoginPageOB.invalidLogin('sdbit04@gmail.com', 'abcd')
        testSetup.invalidLogin('sdbit04@gmail.com', 'abcd')
        # Element, TorF=LoginPageOB.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        Element, TorF=testSetup.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        assert TorF == True
"""

"""
#2nd way of using fixture to create object of class under test
class TestLoginClass:

    def test_invalidLogin(self,onetimeSetup, testSetup):
        # LoginPageOB.invalidLogin('sdbit04@gmail.com', 'abcd')
        testSetup.invalidLogin('sdbit04@gmail.com', 'abcd')
        # Element, TorF=LoginPageOB.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        Element, TorF=testSetup.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        assert TorF == True
"""

"""
3rd way of using fixture to create object of class under test
"""
from PagePkg import LoginPage

class TestLoginClass:

    testSetup=LoginPage.LoginPage("firefox")

    def test_invalidLogin(self):
        # LoginPageOB.invalidLogin('sdbit04@gmail.com', 'abcd')
        self.testSetup.invalidLogin('sdbit04@gmail.com', 'abcd')
        # Element, TorF=LoginPageOB.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        Element, TorF = self.testSetup.getElementWithResult("xpath", "//div[contains(text(), 'Invalid email or password')]")
        assert TorF == True
