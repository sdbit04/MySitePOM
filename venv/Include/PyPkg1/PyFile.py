from selenium import webdriver
import os
location="E:\Python\Developement\BrowserDriver"
os.environ["webdriver.firefox.driver.driver"]=location

driverFF = webdriver.Firefox(location)
driverFF.get("http://www.google.com/")
#The methode bellow return the element, it the tag some specific attributes.
elementById=driverFF.find_element_by_id("lst-ib")
text1=elementById.text
if elementById is not None:
    print("Element was found" + text1)
