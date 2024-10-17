from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from core import environment
from core.AppTest import AppTest
from core.ChromeDriverSettings import ChromeDriverSettings
from utils import string_utils


class LoginPageTest(AppTest):
    def initialize_driver(self):
        self.driverSettings = ChromeDriverSettings()
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
        #                                options=self.driverSettings.get_options())

        chrome_driver_path = "/usr/bin/chromedriver"

        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=self.driverSettings.get_options())
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

        # signin_google_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in with Google')]")

        assert signup_link is not None
        assert forget_password_link is not None
        assert login_button is not None
        # assert signin_google_button is not None
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

        # check whether login is successful
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

        # check whether signup is successful
        my_profile = self.driver.find_element(By.XPATH, "//span[text() = 'My Profile']")

        assert my_profile is not None

    def pass_landing_page(self):
        self.driver.get(environment.target_url())

        self.accept_cookies()

        btn_login = self.driver.find_element(By.XPATH, "//button[text() = 'Log in']")

        btn_login.click()


if __name__ == "__main__":
    LoginPageTest.main()
