from core.DriverSettings import DriverSettings
from selenium.webdriver.chrome.options import Options


class ChromeDriverSettings(DriverSettings):

    def get_options(self):
        chrome_options = Options()
        chrome_options.add_argument('--verbose')
        chrome_options.add_argument("--headless")  # Ensure GUI is off
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")  # Optional, recommended in some environments
        chrome_options.add_argument("--incognito")  # Run in incognito mode
        return chrome_options
