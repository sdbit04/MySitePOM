from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.common.exceptions import ElementNotSelectableException
#
# FireFoxDriverLoc="E:\\Python\\Developement\\BrowserDriver"
# os.environ["webdriver.firefox.driver"]=FireFoxDriverLoc
# Driver=webdriver.Firefox(FireFoxDriverLoc)

# ChromeDriverLoc="E:\\Python\\Developement\\BrowserDriver\\chromedriver.exe"
ChromeDriverLoc="E:\\Python\\Developement\\BrowserDriver\\New\\chromedriver.exe"
os.environ["webdriver.chrome.driver"]=ChromeDriverLoc
Driver=webdriver.Chrome(ChromeDriverLoc)
Driver.implicitly_wait(10)
BaseUrl="https://learn.letskodeit.com/p/practice"
Driver.get(BaseUrl)
Driver.maximize_window()
# The next element has tagName = select, we can instanceiate Select class for the same
DropElement=Driver.find_element(By.XPATH, "//select[@id='carselect']")
SelectElement=Select(DropElement)
SelectElement.select_by_visible_text("Benz")
time.sleep(3)
NameField=Driver.find_element(By.ID, 'name')
NameField.send_keys('swapan')
time.sleep(4)
Driver.close()
