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

    def test_reset_password(self):
        self.driver.get("%s%s" % (self.live_server_url, "/login/"))
        self.driver.execute_script("window.scrollTo(0,900)")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="login"]/div/form/small/a'))).click()
        email_input = self.driver.find_element_by_id("id_email")
        email_input.send_keys("user1@gmail.com")
        self.driver.execute_script("window.scrollTo(0,900)")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="login"]/div/form/button'))).click()