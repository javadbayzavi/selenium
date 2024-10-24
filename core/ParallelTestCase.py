from concurrent.futures import ThreadPoolExecutor
from core.DriverOptionProvider import get_drvier_option
from core.HubLocator import active_browsers
from core.AppTest import AppTest
from core import environment
from selenium.common.exceptions import WebDriverException, InvalidSessionIdException
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry  # Updated import path for Re

from concurrent.futures import ThreadPoolExecutor
import urllib3
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

# Adjust the connection pool size
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CustomRemoteConnection(RemoteConnection):
    def __init__(self, *args, **kwargs):
        # Increase connection pool size
        self.pool = urllib3.PoolManager(num_pools=10, maxsize=10)
        super().__init__(*args, **kwargs)


class ParallelTestCase(AppTest):
    driver = None
    active_nodes = []

    def initialize_driver(self):
        pass

    def run(self, result=None):
        hub_url = environment.get_hub_url()
        self.active_nodes = active_browsers(hub_url)


        # Create a ThreadPoolExecutor to run tests in parallel
        with ThreadPoolExecutor(max_workers=len(self.active_nodes)) as executor:
            futures = []
            # Loop through each browser and run tests
            for browser_name in self.active_nodes:
                # webdriver.RemoteConnection = CustomRemoteConnection
                # Set the session to the WebDriver
                webdriver.Remote.command_executor_class = requests.Session()
                # Submit each test method for parallel execution
                self.set_driver(get_drvier_option(browser_name))
                futures.append(executor.submit(self._run_test_in_parallel, self._testMethodName, result))

            # Wait for all tests to complete and collect results
            for future in futures:
                try:
                    future.result()  # Raises exceptions if any test fails
                except Exception as e:
                    result.addError(self, e)  # Handle errors

        super().run(result)

    def cool_down(self):
        pass

    def _run_test_in_parallel(self, test_method, result):
        self.driver.implicitly_wait(40)
        try:
            getattr(self, test_method)()
        except Exception as e:
            print("Error while running the test" + self.__class__, '_webdriver_type')
            result.addError(self, e)  # This should work correctly
        finally:
            if self.driver is not None:
                try:
                    self.driver.quit()
                except InvalidSessionIdException as e:
                    result.addError(self, e)