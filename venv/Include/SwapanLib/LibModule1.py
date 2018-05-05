from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CustomDriver(object):
    """
    This class has methodes to create different type of driver object.
    CreateCustomDriver() creates WebDriver instance for different browser
    CreateDriverWaitOb() takes the WebDriver instance as argument and creates WebDriverWait object
    createWaitElement() takes WebDriverWait object, LocatorType and Locator to find an object. and a condition.
    :return ElementDriver object while the condition has been satisfied.
    """
    def __init__(self):
        pass
    ChromeDriverLoc="E:\\Python\\Developement\\BrowserDriver\\chromedriver.exe"
    FireFoxDriverLoc="E:\\Python\\Developement\\BrowserDriver"
    IEDriverLoc="E:\\Python\\Developement\\BrowserDriver"

    @classmethod
    def CreateCustomDriver(cls,BrowserName):
    # def CreateCustomDriver(BrowserName):
        """
        This method takes Browser name like Firefox, IE, and Chrome,
        :return corresponding webdriver
        """
        BName=BrowserName  #Parameters are also local viable, it was not defined at class level
        if BName=="Chrome":
            os.environ["webdriver.chrome.driver"]=cls.ChromeDriverLoc
            Driver=webdriver.Chrome(cls.ChromeDriverLoc)

        elif BName=="FireFox":
            os.environ["webdriver.firefox.driver"]=cls.FireFoxDriverLoc
            Driver=webdriver.Firefox(cls.FireFoxDriverLoc)

        elif BName=="IE":
            os.environ["webdriver.ie.driver"]=cls.IEDriverLoc
            Driver=webdriver.Ie(cls.IEDriverLoc)
        else:
            os.environ["webdriver.chrome.driver"] = cls.ChromeDriverLoc
            Driver = webdriver.Chrome(cls.ChromeDriverLoc)
        return Driver
#for Class method decoration is must
    @classmethod
    def CreateDriverWaitOb(cls, Driver, timeout, poll_frequency, ignored_exceptions):
        WebDriverWaitOB=WebDriverWait(driver=Driver, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions)
        return WebDriverWaitOB

    @classmethod
    def createWaitElement(cls, WebDriverWaitObject, CondAbvreation, LocatorType, locator):
        locator1=locator
        CondMethod=Conveter.ConvCondMethod(CondAbvreation)
        Bytype =Conveter.ConvByType(LocatorType)
        try:
            WaitDriverElement=WebDriverWaitObject.until(CondMethod((Bytype, locator1)))
            print("Element was appared within wait time")

        except:
            print("Element was not appeared")
            print_stack()
        return WaitDriverElement

        # WaitElement = WebDriverWaitObject.until((CondMethod((Bytype, locator))))
        # return WaitElement

    driver = CreateCustomDriver("FireFox")

    # driver.find_element()
    @classmethod
    def createElement(cls, Driver, LocatorType, Locator):
        Element=None
        ByType =Conveter.ConvByType(LocatorType)
        try:
            Element=Driver.find_element(ByType, Locator)
            print("Element was found")

        except:
            print("element was not found")

        return Element

class Conveter(object):
    @classmethod
    def ConvByType(cls,ByType):
        ByTyp=ByType
        if ByTyp=="ID":
            return By.ID
        elif ByType=="XPATH":
            return By.XPATH
        else:
            return False

    @classmethod
    def ConvCondMethod(cls,MethABVR):
        MethdAbvr=MethABVR
        ConditioinDictn = {'ETBC': 'element_to_be_clickable', 'TC': 'title_contains', 'UCh': 'url_changes',
                           'UCon': 'url_contains', 'VOEL': 'visibility_of_element_located',
                           'POEL': 'presence_of_element_located'}
        ABVRList = [ConditioinDictn.keys()]
        if MethdAbvr == 'ETBC':
            return EC.element_to_be_clickable
        elif MethdAbvr == 'TC':
            return EC.title_contains
        elif MethdAbvr == 'UCh':
            return EC.url_changes
        elif MethdAbvr == 'VOEL':
            return EC.visibility_of_element_located
        else:
            print("Condtion is not in " + str(ABVRList))
            print(ABVRList)
            return False


class DebugSw(object):
        def __init__():
            pass

        @classmethod
        def takeScreenShort(cls, Driver):
            fname="pic.png"
            DestinationDir="E:\\Python\\Developement\\Selenium\\Test1\\venv\\ScreenShots"
            DestiFile=DestinationDir + fname
            Driver.save_screenshot(DestiFile)
            print("ScreenShots taken")

