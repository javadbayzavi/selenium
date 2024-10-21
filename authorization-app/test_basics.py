import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from concurrent.futures import ThreadPoolExecutor

class ParallelSeleniumTests(unittest.TestCase):
    
    def setUp(self):
        # Specify the desired capabilities for different browsers
        #TODO: This must be taken from url
        self.hub_url = 'http://selenium-hub:4444/wd/hub'
        browser = self.browser

        if browser == "chrome":
            self.capabilities = DesiredCapabilities.CHROME.copy()
        elif browser == "firefox":
            self.capabilities = DesiredCapabilities.FIREFOX.copy()

        self.driver = webdriver.Remote(
            command_executor=self.hub_url,
            desired_capabilities=self.capabilities
        )
        self.driver.implicitly_wait(10)
    
    def test_open_page(self):
        self.driver.get("http://example.com")
        self.assertIn("Example Domain", self.driver.title)

    def tearDown(self):
        self.driver.quit()

def run_test_in_parallel(browser):
    suite = unittest.TestSuite()
    suite.addTest(ParallelSeleniumTests("test_open_page"))
    ParallelSeleniumTests.browser = browser  # Set browser dynamically
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    browsers = ["chrome", "firefox"]  # You can add more browsers here

    # Run tests in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
        futures = [executor.submit(run_test_in_parallel, browser) for browser in browsers]