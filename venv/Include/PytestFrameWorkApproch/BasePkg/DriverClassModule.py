from selenium import webdriver
import os
from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

#Framework: I will create Driver using the class DriverCreator::createDriver()
class DriverCreator(object):
    @classmethod
    def createDriver(cls, Browser):
        cls.Browser = Browser

        if cls.Browser.lower() == "chrome":
            cls.DriverLocation="E:\\Python\\Developement\\BrowserDriver\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"]=cls.DriverLocation
            cls.Driver=webdriver.Chrome(cls.DriverLocation)
        elif cls.Browser.lower() == "firefox":
            cls.DriverLocation="E:\\Python\\Developement\\BrowserDriver"
            os.environ["webdriver.firefox.driver"]=cls.DriverLocation
            cls.Driver=webdriver.Firefox(cls.DriverLocation)
        elif cls.Browser.lower() == "ie":
            cls.DriverLocation="E:\\Python\\Developement\\BrowserDriver\\MicrosoftWebDriver.exe"
            os.environ["webdriver.ie.driver"]=cls.DriverLocation
            cls.Driver=webdriver.Firefox(cls.DriverLocation)
        else:
            print("Browser name should be in Chrome, Ie, or Firefox")
            cls.Driver=None
        try:
            cls.tmpurl=cls.Driver.current_url

        except:
            print("Driver was not found for browser " + cls.Browser)
            print_stack()

        return cls.Driver


#Framework: I will create an object of this class for the Driver object we get from the above class
#Framework: I will define multiple utility methodes those will use this Driver as an instance attribute of the object of following class
class SelenumDriver(object):
    def __init__(self,Browser):
        self.timeout = 30
        self.Driver=DriverCreator.createDriver(Browser)
        self.Driver.implicitly_wait(4)
        self.WaitDriver=WebDriverWait(driver=self.Driver,timeout=self.timeout,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
        print("during construction of SeleniumDriver object, we have created: object of WebDriver=Driver, & an object of WebDriverWait=WaitDriver with timeout=" + str(self.timeout))

    # def creteWaitDriver(self, timeout):
    #     WaitDriver=WebDriverWait(driver=self.Driver,timeout=timeout,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])


    #Next methode is a helping hand for all the follwing methodes
    @staticmethod
    def getBytype(LocatorType):
        if LocatorType.lower()=='id':
            return By.ID
        elif LocatorType.lower()=='xpath':
            return By.XPATH
        elif LocatorType.lower()=='link':
            return By.LINK_TEXT
        elif LocatorType.lower()=='class':
            return By.CLASS_NAME
        elif LocatorType.lower()=='css':
            return By.CSS_SELECTOR
        else:
            print("LocatorType is invalid, valid list is id, xpath, link, class, css")
            return
    @staticmethod
    def conditionWrapper(CondABVR):
        #conditionList=['element_to_be_clickable', 'title_contains','url_changes','url_contains','visibility_of_element_located','presence_of_element_located','element_located_to_be_selected','element_located_selection_state_to_be','element_selection_state_to_be','element_to_be_selected','frame_to_be_available_and_switch_to_it','invisibility_of_element_located','visibility_of_element_located','presence_of_all_elements_located','url_matches','visibility_of_all_elements_located','visibility_of_any_elements_located']
        ConditioinDictn={'ETBC':'element_to_be_clickable', 'TC':'title_contains','UCh':'url_changes','UCon':'url_contains','VOEL':'visibility_of_element_located','POEL':'presence_of_element_located'}
        ABVRList=[ConditioinDictn.keys()]
        if CondABVR == 'ETBC':
            return EC.element_to_be_clickable
        elif CondABVR == 'TC':
            return EC.title_contains
        elif CondABVR =='UCh':
            return EC.url_changes
        elif CondABVR == 'VOEL':
            return EC.visibility_of_element_located
        else:
            print("Condtion is not in " + str(ABVRList))
            print(ABVRList)
            return False


        #Based on MethodeABVR this will return expected condition to start working on an element
    def getWaitDriverElement(self,CondMethodABVR, Locatortype, Locator):
        CondMethod=SelenumDriver.conditionWrapper(CondMethodABVR)
        ByType=SelenumDriver.getBytype(Locatortype)
        try:
            WaitDriverElement=self.WaitDriver.until(CondMethod((ByType, Locator)))
            print("Element was appared within wait time")
        except:
            print("Element was not appeared")
            print_stack()
            exit()
        return WaitDriverElement

    #follwing method has no decocrator, like @classmethod or @staticmethod, so it is a instance method
    def getElementWithResult(self,LocatorType, Locator):
        Element=None
        result=False
        print("getting element:" + str(Locator))
        ByType=self.getBytype(LocatorType)
        try:
            Element=self.Driver.find_element(ByType, Locator)
            result=True
            print("Element was found")
        except:
            # If it can handle the exception then only it navigate to except block
            Element=None
            result=False
            print("exception occure")
        return Element, result



    def clickElement(self, LocatorType, Locator):
        print("Clicking element:" + str(Locator))
        self.getElement(LocatorType, Locator).click()

    def clickElementWithResult(self, LocatorType, Locator):
        Element, Result=self.getElementWithResult(LocatorType, Locator)
        if Result:
            Element.click()
        else:
            self.Driver.close()


    def waitNclickElement(self, condABVR, LocatorType, Locator):
        print("Clicking element:" + str(Locator))
        self.getWaitDriverElement(condABVR, LocatorType, Locator).click()

    def waitNsendKyes(self,condABVR, LocatorType, Locator, keys):
        waitElementField=self.getWaitDriverElement(condABVR, LocatorType, Locator)
        waitElementField.send_keys(keys)

# SelenumDriverOB=SelenumDriver("Chrome")
# SelenumDriverOB.Driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')
# SelenumDriverOB.waitNclickElement('ETBC','XPATH', '//input[@type="submit"]')

# Driver=webdriver.Chrome()
# E1=Driver.find_element(By.ID, 'ab')
# E1.send_keys()
