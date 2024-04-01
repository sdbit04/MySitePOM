from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as ChromService
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:

    def __init__(self, driver_instance: Chrome):
        self.driver = driver_instance

    def open_login_page(self):
        self.driver.get("https://www.google.com/")


driver_instance = Chrome(service=ChromService(ChromeDriverManager().install()))

login_page = LoginPage(driver_instance)
login_page.open_login_page()


