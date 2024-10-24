import logging
import unittest
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from core.DriverSettings import DriverSettings

logging.basicConfig(level=logging.INFO)


class AppTest(ABC, unittest.TestCase):
    driver = None

    driverSettings: DriverSettings

    @abstractmethod
    def initialize_driver(self):
        pass

    @abstractmethod
    def cool_down(self):
        pass

    def setUp(self):
        self.initialize_driver()

    def tearDown(self):
        self.cool_down()

    def set_driver(self, driver):
        self.driver = driver

    def accept_cookies(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.find_element(By.XPATH, "//div[contains(text(),'Accept all')]") is not None)
        self.driver.find_element(By.XPATH, "//div[text() = 'Accept all']").click()
