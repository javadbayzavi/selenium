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

    def setUp(self):
        self.initialize_driver()
        if not self.driverSettings.is_headless():
            self.driver.minimize_window()

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def accept_cookies(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.find_element(By.XPATH, "//div[contains(text(),'Accept all')]") is not None)
        self.driver.find_element(By.XPATH, "//div[text() = 'Accept all']").click()
