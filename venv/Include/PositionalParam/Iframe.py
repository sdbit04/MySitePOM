from Include.PytestFrameWorkApproch.BasePkg.DriverClassModule import SelenumDriver
import time
SDriver=SelenumDriver("firefox")
SDriver.Driver.get("https://learn.letskodeit.com/p/practice")
SDriver.Driver.execute_script("window.scrollBy(0, 1000);")
SDriver.Driver.switch_to_frame("courses-iframe")
Search, STorF=SDriver.getElementWithResult('xpath', "//input[@id='search-courses']")
if STorF:
    Search.send_keys("Python")
else:
    print("Element was not found")

time.sleep(4)
SDriver.Driver.close()