from  Include.SwapanLib.LibModule1 import *
from Include.SwapanLib.LibModule1 import CustomDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from Include.SwapanLib.LibModule1 import DebugSw
BaseURL="https://www.expedia.co.in"
Driver=CustomDriver.CreateCustomDriver("Chrome")
Driver.get(BaseURL)
WebDriverWaitOB=CustomDriver.CreateDriverWaitOb(Driver, 20, 1, [ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
LocationSearch=Driver.find_element_by_id("hotel-destination")
LocationSearch.send_keys("Kol")
SearchList=CustomDriver.createWaitElement(WebDriverWaitOB,"VOEL","XPATH",'//div[@class="display-group-results"]')
SearchList.find_element_by_xpath('//li[@data-tid="typeahead-item1"]').click()
#
# , '//div[@class="display-group-results"]')

# ---------------
CheckInDateElement=Driver.find_element(By.XPATH, '//label[@for="hotel-checkin"]//span[@class="icon icon-calendar"]')
CheckInDateElement.click()
ActiveMonth=CustomDriver.createWaitElement(WebDriverWaitOB,"VOEL","XPATH", "//div[@class='datepicker-cal-month'][position()=1]//tbody[@class='datepicker-cal-dates']")
ActiveDates=ActiveMonth.find_elements(By.XPATH, "//button[@class='datepicker-cal-date']")
for ActiveDate in ActiveDates:
    if ActiveDate.text=='26':
        ActiveDate.click()
        break
# ----------------
CheckOutDateElement=Driver.find_element(By.XPATH, '//label[@for="hotel-checkout"]//span[@class="icon icon-calendar"]')
CheckOutDateElement.click()
ActiveMonth=CustomDriver.createWaitElement(WebDriverWaitOB,"VOEL","XPATH", "//div[@class='datepicker-cal-month'][position()=2]//tbody[@class='datepicker-cal-dates']")
ActiveDates=ActiveMonth.find_elements(By.XPATH, "//button[@class='datepicker-cal-date']")
for ActiveDate in ActiveDates:
    if ActiveDate.text=='28':
        ActiveDate.click()
        break
# ------------------
SearchButton=CustomDriver.createWaitElement(WebDriverWaitOB, "ETBC", "ID", "search-button")
SearchButton.click()

DebugSw.takeScreenShort(Driver)
