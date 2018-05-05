from Include.PytestFrameWorkApproch.BasePkg.DriverClassModule import DriverCreator
Driver=DriverCreator.createDriver("firefox")
Driver.implicitly_wait(7)
from selenium.webdriver.common.by import By
import time
Driver.get("https://learn.letskodeit.com/p/practice")
ParentHandle=Driver.current_window_handle
print("Parent handle is " + ParentHandle)
# clickElementWithResult('xpath', "//button[@id='openwindow']")

OpenWindow=Driver.find_element(By.ID, 'openwindow')
OpenWindow.click()
handles=Driver.window_handles
for handle in handles:
    print("Handles are " + handle)
for handle in handles:
    if handle not in ParentHandle:
        Driver.switch_to.window(handle)
        print ("Child window handle is " + handle)
        SearchCourse=Driver.find_element(By.XPATH, "//input[@id='search-courses']")
        # if SearchCourceTorF:
        SearchCourse.send_keys("Python")
        time.sleep(6)
        Driver.close()
        break

Driver.switch_to.window(ParentHandle)
time.sleep(3)
NewTab=Driver.find_element(By.XPATH, "//a[@id='opentab']")
NewTab.click()

