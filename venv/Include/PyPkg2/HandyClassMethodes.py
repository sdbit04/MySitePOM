from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

class HandyClass(object):
    def __init__(self):
        #No param constructor
        pass
    def createCustomDriver(BrowserTypeP):
        BrowserType=BrowserTypeP
        if BrowserType == "Chrome":
            driverLocation="E:\\Python\\Developement\\BrowserDriver\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"]=driverLocation
            Driver=webdriver.Chrome(driverLocation)
            return Driver
        elif BrowserType == "Firefox":
            driverLocation="E:\\Python\\Developement\\BrowserDriver"
            os.environ["webdriver.firefox.driver"]=driverLocation
            Driver=webdriver.Firefox(driverLocation)
            return Driver
        else:
            print("Browser type is not found")
            return False

#Next one is an independent function
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
        elif CondABVR== 'VOEL':
            return EC.visibility_of_element_located
        else:
            print("Condtion is not in " + str(ABVRList))
            print(ABVRList)
            return False

    def creteWaitDriverElement(CustomDriver, timeout, MethodABVR, ByType, Locator):
        WaitDriver=WebDriverWait(driver=CustomDriver,timeout=timeout,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
        #Based on MethodeABVR this will return expected condition to start working on an element
        CondMethod=HandyClass.conditionWrapper(MethodABVR)
        try:
            WaitDriverElement=WaitDriver.until(CondMethod((ByType, Locator)))
            print("Element was appared within wait time")
        except:
            print("Element was not appeared")
            print_stack()
            exit()
        return WaitDriverElement


if __name__ == "__main__":
    ConditionToPrint = HandyClass.conditionWrapper('ETBC')
    print("Method retured : " + str(ConditionToPrint))
    #HandyObject=HandyClass()
    FirefoxDriver=HandyClass.createCustomDriver("Firefox")
    FirefoxDriver.get("https://letskodeit.teachable.com/p/practice")
    Element2=FirefoxDriver.find_element(By.XPATH, "//a[@class='navbar-link fedora-navbar-link']")
    Element2.click()
    Element3=HandyClass.creteWaitDriverElement(FirefoxDriver, 20, 'ETBC', By.ID, 'user_email')
    Element3.send_keys("sdbit04@gmail.com")
