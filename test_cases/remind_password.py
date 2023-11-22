import os
import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class TestRemindPassword(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_failure_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.click_on_remind_password_button()
        user_login.type_in_remind_email('zacnieskadrowane@gmail.com')
        time.sleep(3)
        user_login.click_on_send_button()
        time.sleep(2)


    @classmethod
    def tearDown(self):
        self.driver.quit()