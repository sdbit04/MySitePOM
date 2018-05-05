from Include.PytestFrameWorkApproch.BasePkg.DriverClassModule import SelenumDriver
SDriver=SelenumDriver("firefox")
import time
SDriver.Driver.get("https://learn.letskodeit.com/p/practice")
ParentHandle=SDriver.Driver.current_window_handle
SDriver.clickElementWithResult('xpath', "//button[@id='openwindow']")
handles=SDriver.Driver.window_handles
for handle in handles:
    if handle != ParentHandle:
        SDriver.Driver.switch_to.window(handle)
        print ("New window handle is " + handle)
        SearchCource, SearchCourceTorF = SDriver.getElementWithResult('xpath', "//input[@id='search-courses']")
        if SearchCourceTorF:
            SearchCource.send_keys("Python")
        time.sleep(6)
        SDriver.Driver.close()

SDriver.Driver.switch_to.window(ParentHandle)
time.sleep(3)
# SDriver.clickElementWithResult('xpath', "//a[@id='opentab']")
SDriver.clickElementWithResult('xpath', "//a[contains(text(), 'Login')]")
