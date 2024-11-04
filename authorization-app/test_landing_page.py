from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from core.TestCase import TestCase
from core import environment
from core.WebDrivers import WebDrivers

@WebDrivers.enforce_webdriver(environment.get_default_driver())
class LandingPageTest(TestCase):
    def test_auth_landing_page(self):
        self.driver.get(environment.target_url())
        self.assertEqual("Studio 3T License Manager", self.driver.title)

    def test_user_sees_privacy_modal(self):
        self.driver.get(environment.target_url())

        wait = WebDriverWait(self.driver, 5)
        wait.until(lambda driver: driver.find_element(By.XPATH, "//div[contains(text(),'Accept all')]") is not None)

        self.driver.find_element(By.XPATH, "//div[text() = 'Accept all']")
        self.driver.find_element(By.XPATH, "//div[text() = 'Decline all']")
        self.driver.find_element(By.XPATH, "//div[text() = 'Manage cookies']")

    def test_auth_see_login_button(self):
        self.driver.get(environment.target_url())

        self.accept_cookies()

        btn_login = self.driver.find_element(By.XPATH, "//button[text() = 'Log in']")

        assert btn_login is not None

    def test_auth_click_login_button(self):
        self.driver.get(environment.target_url())

        self.accept_cookies()

        btn_login = self.driver.find_element(By.XPATH, "//button[text() = 'Log in']")

        btn_login.click()

        self.assertEqual("Studio 3T Login", self.driver.title)

    def test_third_party_sso(self):
        self.driver.get(environment.target_url())

        self.accept_cookies()

        btn_sso = self.driver.find_element(By.XPATH, "//button[text() = 'Third party single sign-on']")

        btn_sso.click()


if __name__ == "__main__":
    LandingPageTest.main()
