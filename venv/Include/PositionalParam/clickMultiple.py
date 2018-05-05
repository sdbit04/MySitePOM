from selenium import webdriver

from Include.SwapanLib.LibModule1 import CustomDriver
from selenium.webdriver.common.by import By
import time
Driver=CustomDriver.CreateCustomDriver("Chrome")
BaseUrl="https://learn.letskodeit.com/p/practice"
Driver.get(BaseUrl)

RadioButtonList=Driver.find_elements(By.XPATH, "//input[@name='cars' and @type='radio']")

print(str(len(RadioButtonList)))

for element in RadioButtonList:
    if not element.is_selected():

        element.click()
        time.sleep(4)



Driver.close()