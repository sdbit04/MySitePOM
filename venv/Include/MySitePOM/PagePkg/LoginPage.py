from selenium.webdriver.common.by import By
from Include.MySitePOM.BasePkg.DriverClassModule import SelenumDriver
import time
class LoginPage(SelenumDriver):
    def __init__(self,Browser):
        super().__init__(Browser)

    # Here we will create an object of LoginPage for WebDriverInstance, and all the method of page object
    # can access the driver instance

    # We also may go to create static class, all of its static methods could take driver as an argument to perform its action
    # That won't be good, we repeatedly need to provide Driver as an argument to all the methodes
    # def getLoginLinkElement(self, Driver)

    _baseUrl="https://letskodeit.teachable.com/"
    _screenShotsDir="E:\\Python\\Developement\\Selenium\\MySitePOM\\venv\\Include\\MySitePOM\\ScreenShots\\invalidLogin.png"
    _loginLink="Login"
    _userEmailID="user_email"
    _passwordXpath='//div[@class="form-group"]//input[@id="user_password"]'
    _submitXpath='//input[@type="submit"]'
    #The above attribute is an class level attribute, but we can access it from an instance level, and change the value of this variable
    # at instance level only. The class level value of the attribute remain same.

    def clickLogin(self):
        # self.getElement('link', self._loginLink).click()
        self.clickElementWithResult('link', self._loginLink)

    def clickSubmit(self):
        self.waitNclickElement('ETBC','XPATH', '//input[@type="submit"]')

    def sendUserId(self, userid):
        self.waitNsendKyes('VOEL', 'id' , self._userEmailID, userid)

    def sendPassword(self, passwrd):
        self.waitNsendKyes('VOEL', 'xpath', self._passwordXpath, passwrd )

    def invalidLogin(self, userid, password):
        self.Driver.get(self._baseUrl)
        # height = self.Driver.execute_script("return window.innerHeight;")
        # # height = self.Driver.execute_script("return window.innerHeight;")
        # width = self.Driver.execute_script("return window.innerWidth;")
        # print("Height: " + str(height))
        # print("Width: " + str(width))
        self.clickLogin()
        self.sendUserId(userid)
        self.sendPassword(password)
        self.clickSubmit()
        winHight=self.Driver.execute_script("return window.innerHeight;")
        print("window hight is = " + str(winHight))
        self.Driver.save_screenshot(self._screenShotsDir)

        # try:
        #     self.Driver.save_screenshot(self._screenShotsDir)
        #     print("ScreenShots taken")
        # except:
        #     print("exception occure")

# LogOB=LoginPage("Chrome")
# LogOB.invalidLogin("asdfb@gmail.com", "asfdarwer")