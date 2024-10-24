from core.ParallelTestCase import ParallelTestCase
from core.TestCase import TestCase
from core.WebDrivers import WebDrivers
from core.WebDrivers import BrowserType
from core import environment

@WebDrivers.enforce_firefox_driver(False)
class MyTestCase(TestCase):
# class MyTestCase(ParallelTestCase):
    def test_example_1(self):
        self.driver.get(environment.target_url())
        self.assertEqual("Studio 3T License Manager", self.driver.title)        
        self.assertTrue(True)

    def test_example_2(self):
        self.assertTrue(True)

    def test_example_3(self):
        self.assertTrue(True)

    def test_example_4(self):
        self.assertTrue(True)
