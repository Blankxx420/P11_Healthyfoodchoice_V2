
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from djangoProject.settings import BASE_DIR
from selenium.webdriver.common.by import By


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True


class SeleniumRegisterTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox(
            executable_path=str(BASE_DIR / 'webdrivers' / 'geckodriver'),
            options=firefox_options,
        )
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_register(self):
        """Launches the functional_tests for the registration and automatical loggin feature"""
        # Access register page and fill fields
        self.driver.get("%s%s" % (self.live_server_url, "/register/"))
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("usertest1@email.com")
        username_input = self.driver.find_element(By.NAME,"username")
        username_input.send_keys("usertest1")
        password_input = self.driver.find_element(By.NAME,"password1")
        password_input.send_keys("Password+1234")
        confirm_password_input = self.driver.find_element(By.NAME, "password2")
        confirm_password_input.send_keys("Password+1234")
        # Click on button which registers + login automatically
        self.driver.execute_script("window.scrollTo(0,900)")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="register"]/div/form/button'))).click()

        # Checks if icon "mon_compte" in DOM, means logged in
        self.driver.find_element(By.ID, "mon_compte")
