import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from core import environment
from core.AppTest import AppTest
from core.ChromeDriverSettings import ChromeDriverSettings
from utils import string_utils

class LoginPageTest(AppTest):
    def initialize_driver(self):
        # Specify the browser capabilities; you can change "chrome" to "firefox", "edge", etc.
        # Define the possible options
        capabilities_options = [DesiredCapabilities.CHROME, DesiredCapabilities.FIREFOX]

        # Randomly select one of the options
        capabilities = random.choice(capabilities_options)


        # Specify the URL of the Selenium Grid hub
        grid_url = "http://selenium-hub:4444/wd/hub"  # Change this if your grid is on a different host

        # Create a Remote WebDriver instance
        self.driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)
        self.driver.implicitly_wait(40)

    def test_see_login_panel(self):
        self.pass_landing_page()

        self.assertEqual("Studio 3T Login", self.driver.title)

        username_text = self.driver.find_element(
            By.XPATH, "//input[@type='text' and contains(@placeholder, 'email')]"
        )
        password_text = self.driver.find_element(
            By.XPATH, "//input[@type='password' and contains(@placeholder, 'password')]"
        )

        login_button = self.driver.find_element(By.XPATH, "//button[text() = 'Sign in']")
        signup_link = self.driver.find_element(By.XPATH, "//a[text() = 'Sign up']")
        forget_password_link = self.driver.find_element(By.XPATH, "//a[text() = 'Forgot your password?']")

        assert signup_link is not None
        assert forget_password_link is not None
        assert login_button is not None
        assert username_text is not None
        assert password_text is not None

    def test_login_with_valid_credentials(self):
        self.pass_landing_page()

        username_text = self.driver.find_element(
            By.XPATH, "//input[@type='text' and contains(@placeholder, 'email')]"
        )
        password_text = self.driver.find_element(
            By.XPATH, "//input[@type='password' and contains(@placeholder, 'password')]"
        )

        login_button = self.driver.find_element(By.XPATH, "//button[text() = 'Sign in']")

        username_text.send_keys("selenium_test@3t.io")
        password_text.send_keys("Selenium_test123")

        login_button.click()

        my_profile = self.driver.find_element(By.XPATH, "//span[text() = 'My Profile']")
        assert my_profile is not None

    def test_login_with_invalid_credentials(self):
        self.pass_landing_page()

        username_text = self.driver.find_element(
            By.XPATH, "//input[@type='text' and contains(@placeholder, 'email')]"
        )
        password_text = self.driver.find_element(
            By.XPATH, "//input[@type='password' and contains(@placeholder, 'password')]"
        )

        login_button = self.driver.find_element(By.XPATH, "//button[text() = 'Sign in']")

        username_text.send_keys("selenium_test@3t.io")
        password_text.send_keys("wrongpassword")

        login_button.click()

        error_message = self.driver.find_element(By.XPATH,
                                                 "//p[text() = 'Your email address or password are incorrect. Please try again, or recover your password.']")
        assert error_message is not None

    def test_user_see_signup(self):
        self.pass_landing_page()

        signup_link = self.driver.find_element(By.XPATH, "//a[text() = 'Sign up']")
        assert signup_link is not None

        signup_link.click()

        email_text = self.driver.find_element(
            By.XPATH, "//input[@type='email' and contains(@placeholder, 'email address')]"
        )
        password_text = self.driver.find_element(
            By.XPATH, "//input[@type='password' and contains(@placeholder, 'password here')]"
        )
        first_name_text = self.driver.find_element(
            By.XPATH, "//input[@type='text' and contains(@placeholder, 'first name here')]"
        )
        last_name_text = self.driver.find_element(
            By.XPATH, "//input[@type='text' and contains(@placeholder, 'last name here')]"
        )
        tel_text = self.driver.find_element(
            By.XPATH, "//input[@type='tel']"
        )
        privacy_checkbox = self.driver.find_element(
            By.XPATH, "//input[@type='checkbox']"
        )

        login_button = self.driver.find_element(By.XPATH, "//button[text() = 'Sign up']")

    def test_user_signup(self):
        self.pass_landing_page()

        signup_link = self.driver.find_element(By.XPATH, "//a[text() = 'Sign up']")
        assert signup_link is not None

        signup_link.click()

        email_text = self.driver.find_element(
            By.XPATH, "//input[@type='email' and contains(@placeholder, 'email address')]"
        )
        password_text = self.driver.find_element(
            By.XPATH, "//input[@type='password' and contains(@placeholder, 'password here')]"
        )
        first_name_text = self.driver.find_element(
            By.XPATH, "//input[@type='text' and contains(@placeholder, 'first name here')]"
        )
        last_name_text = self.driver.find_element(
            By.XPATH, "//input[@type='text' and contains(@placeholder, 'last name here')]"
        )
        tel_text = self.driver.find_element(
            By.XPATH, "//input[@type='tel']"
        )
        privacy_checkbox = self.driver.find_element(
            By.XPATH, "//input[@type='checkbox']"
        )

        login_button = self.driver.find_element(By.XPATH, "//button[text() = 'Sign up']")

        email_text.send_keys(string_utils.generate_random_email())
        password_text.send_keys(string_utils.generate_random_password())
        first_name_text.send_keys("Selenium")
        last_name_text.send_keys("Test")
        tel_text.send_keys("1234567890")
        privacy_checkbox.click()
        login_button.click()

        my_profile = self.driver.find_element(By.XPATH, "//span[text() = 'My Profile']")
        assert my_profile is not None

    def pass_landing_page(self):
        self.driver.get(environment.target_url())

        self.accept_cookies()

        btn_login = self.driver.find_element(By.XPATH, "//button[text() = 'Log in']")
        btn_login.click()

if __name__ == "__main__":
    LoginPageTest.main()