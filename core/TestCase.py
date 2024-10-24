
from core.DriverOptionProvider import get_drvier_option
from core.AppTest import AppTest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from core.ChromeDriverSettings import ChromeDriverSettings
from core.FirefoxDriverSettings import FirefoxDriverSettings

class TestCase(AppTest):
    def initialize_driver(self):
        # Read the class-level WebDriver configuration set by the decorator
        webdriver_type = getattr(self.__class__, '_webdriver_type', "chrome")
        is_local = getattr(self.__class__, '_is_local', False)

        # Set the appropriate WebDriver based on the configuration
        if webdriver_type == "chrome":
            if is_local:
                chrome_driver_path = "/usr/bin/chromedriver"
                cservice = Service(chrome_driver_path)
                self.driver = webdriver.Chrome(service=cservice, options=ChromeDriverSettings().get_options())
            else:
                # Initialize a remote Chrome WebDriver (Selenium Grid)
                self.driver = get_drvier_option(webdriver_type)

        elif webdriver_type == "firefox":
            if is_local:
                firefox_driver_path = "/usr/bin/geckodriver"
                fservice = FirefoxService(firefox_driver_path)
                self.driver = webdriver.Firefox(service=fservice, options=FirefoxDriverSettings().get_options())
            else:
                # Initialize a remote Firefox WebDriver (Selenium Grid)
                self.driver = get_drvier_option(webdriver_type)

        # Add more conditions for other browsers (EDGE, SAFARI)

        self.driver.implicitly_wait(40)
    
    def cool_down(self):
        if self.driver is not None:
            self.driver.quit()
