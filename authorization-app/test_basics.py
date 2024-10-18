from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browsers = {
    'chrome': DesiredCapabilities.CHROME,
    'firefox': DesiredCapabilities.FIREFOX,
    'edge': DesiredCapabilities.EDGE,
    'safari': DesiredCapabilities.SAFARI
}

# Loop through each browser
for browser_name, capabilities in browsers.items():
    grid_url = "http://selenium-hub:4444/wd/hub"  # Change if needed

    driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)

    #it will continue if it cannot find the driver    
    if driver == None: 
        continue

    try:
        # Your test code here
        driver.get("http://example.com")
        print(f"{browser_name} Title:", driver.title)

    finally:
        driver.quit()  # Close the browser