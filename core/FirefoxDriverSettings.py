from core.DriverSettings import DriverSettings
from selenium.webdriver.firefox.options import Options


class FirefoxDriverSettings(DriverSettings):
    def __init__(self):
        super().__init__()

    def get_options(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Ensure GUI is off
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--disable-gpu")  # Optional, recommended in some environments
        firefox_options.add_argument("--incognito")  # Run in incognito mode
        return firefox_options
