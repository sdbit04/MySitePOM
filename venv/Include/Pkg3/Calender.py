from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from Include.PyPkg2.HandyClassMethodes import HandyClass #not is use
BaseUrl="https://www.expedia.co.in"
# driverLocation="E:\\Python\\Developement\\BrowserDriver\\chromedriver.exe"
# os.environ["webdriver.chrome.driver"]=driverLocation
# Driver=webdriver.Chrome(driverLocation)
# Driver.implicitly_wait(10) #this is not good practice, i have use used to concentrate into calender only
# Driver.get("https://www.expedia.co.in")
# CheckInDateElement=Driver.find_element(By.XPATH, '//label[@for="hotel-checkin"]//span[@class="icon icon-calendar"]')
# CheckInDateElement.click()
#
# ActiveDates=Driver.find_elements(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]//tbody[@class='datepicker-cal-dates']//button[@class='datepicker-cal-date']")

Driver=HandyClass.createCustomDriver("Chrome")
Driver.get(BaseUrl)
CheckInDateElement=Driver.find_element(By.XPATH, '//label[@for="hotel-checkin"]//span[@class="icon icon-calendar"]')
CheckInDateElement.click()
ActiveMonth=HandyClass.creteWaitDriverElement(Driver, 20, 'VOEL',By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]//tbody[@class='datepicker-cal-dates']" )

ActiveDates=ActiveMonth.find_elements(By.XPATH, "//button[@class='datepicker-cal-date']")

for ActiveDate in ActiveDates:
    if ActiveDate.text=='26':
        ActiveDate.click()
        break
