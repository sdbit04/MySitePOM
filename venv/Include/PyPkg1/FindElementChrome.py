from selenium import webdriver
import os
class ElementFinder():
   def __init__(self,Browser):

       self.Browser=Browser
       if self.Browser=="Chrome":
            self.Location = "E:\\Python\\Developement\\BrowserDriver\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = self.Location #self.Location mean Location attribute of the instance created.
            self.ChromDriver = webdriver.Chrome(self.Location)
       elif self.Browser=="Firefox":
            self.Location = "E:\\Python\\Developement\\BrowserDriver"
            os.environ["webdriver.firefox.driver"] = self.Location
            self.ChromDriver = webdriver.Firefox(self.Location)

   def findElementID(self):
       """
       This method works based on an instance of ElementFinder based on Browser type.
       Try to find an element on the web-page and return 0 if successfully idenfied the required element
       """
       self.ChromDriver.get("https://letskodeit.teachable.com/p/practice")
       ElementByID=self.ChromDriver.find_element_by_id("carselect")
       if ElementByID is not None:
           print("Found element by id")

   def findElementLink(self):
        """
        This method works based on an instances of ElementFinder based on Browser type
        Try to find an elememnt based on the link-text
        In this case deiver serach for an ancchor tag <a/> having some text, say Login
        :return:
        """
        self.ChromDriver.get("https://letskodeit.teachable.com/p/practice")
        ElementByLink=self.ChromDriver.find_element_by_link_text("Login")
        if ElementByLink is not None:
            EBLText=ElementByLink.text
            print("Element was found by link " + EBLText)

#Create object for Chrome and run methdes
ElementFinderChrom=ElementFinder("Chrome")
#ElementFinderChrom.findElementID()
ElementFinderChrom.findElementLink()

#Create object for firefox and run methodes
ElementFinderFirefox=ElementFinder("Firefox")
#ElementFinderFirefox.findElementID()
#help(ElementFinderFirefox.findElementID()) #Here help() work onthe return value of the methode findElementID(), and it is null this case.
#help(ElementFinderFirefox.findElementID)
