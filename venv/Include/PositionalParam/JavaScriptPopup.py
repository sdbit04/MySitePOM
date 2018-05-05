
from Include.PytestFrameWorkApproch.BasePkg.DriverClassModule import SelenumDriver
import time
SDriver=SelenumDriver("firefox")
SDriver.Driver.implicitly_wait(4)
driver=SDriver.Driver
driver.get("https://learn.letskodeit.com/p/practice")
SDriver.waitNsendKyes('VOEL','id', 'name', 'swapan')
time.sleep(3)
SDriver.clickElementWithResult('xpath', "//input[@id='alertbtn']")
time.sleep(3)
alert=driver.switch_to.alert
alert.accept()
time.sleep(3)
driver.close()

