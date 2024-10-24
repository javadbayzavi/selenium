from selenium import webdriver  # Ensure you import the necessary WebDriver classes
from core.HubLocator import active_browsers
from core.ChromeDriverSettings import ChromeDriverSettings
from core.FirefoxDriverSettings import FirefoxDriverSettings
from core import environment

def get_drvier_option(name="chrome"):
    driver = None
    hub_url = environment.get_hub_url()

    # Initialize the WebDriver based on the selected browser
    if name == "" or name is None:
        raise ValueError(f"Unsupported browser: {name}")
    else:
        driver = webdriver.Remote(
            command_executor=hub_url,
            options= get_driver_setting(name=name).get_options()
        )
    
    return driver

def get_driver_setting(name="chrome"):
    driver_setting = None

    if name == "chrome":
        driver_setting = ChromeDriverSettings()

    elif name == "firefox":
        driver_setting = FirefoxDriverSettings()
    else:
        raise ValueError(f"Unsupported browser: {name}")
    
    return driver_setting
    
