import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_FIELD_XPATH = "//*[@id='login']"
    PASSWORD_FIELD_XPATH = "//*[@id='password']"
    SING_IN_BUTTON_XPATH = "//*[text()='Sign in']"
    LOGIN_URL = 'https://dareit.futbolkolektyw.pl/en'
    EXPECTED_TITLE = "Scouts panel - sign in"
    TITLE_OF_BOX_XPATH = "//*[@id='__next']/from/div/div[1]/h5"
    HEADER_OF_BOX = 'Scouts Panel'
    SING_OUT_BUTTON_XPATH = "//div/span[text()='Logout']"
    CHANGE_LANGUAGE_BUTTON_XPATH = "//div/span[text()='Polski']"
    EXPECTED_VALIDATION_INFO = "Identifier or password invalid."
    EXPECTED_VALIDATION_INFO_XPATH = "//span[text()='Identifier or password invalid.']"
    REMIND_PASSWORD_BUTTON_XPATH = "//div/a[text()='Remind password']"
    REMIND_EMAIL_FIELD_XPATH = "//input"

    def type_in_email(self, email):
        self.field_send_keys(self.LOGIN_FIELD_XPATH, email)

    def type_in_remind_email(self, email):
        self.field_send_keys(self.REMIND_EMAIL_FIELD_XPATH, email)

    def type_in_password(self, password):
        self.field_send_keys(self.PASSWORD_FIELD_XPATH, password)

    def click_on_the_sing_in_button(self):
        self.click_on_the_element(self.SING_IN_BUTTON_XPATH)

    def click_on_send_button(self):
        self.click_on_the_element(self.REMIND_EMAIL_FIELD_XPATH)

    def title_of_page(self):
        assert self.get_page_title(self.LOGIN_URL) == self.EXPECTED_TITLE

    def click_on_the_sing_out_button(self):
        self.click_on_the_element(self.SING_OUT_BUTTON_XPATH)

    def click_on_change_language_button(self):
        self.click_on_the_element(self.CHANGE_LANGUAGE_BUTTON_XPATH)

    def click_on_remind_password_button(self):
        self.click_on_the_element(self.REMIND_PASSWORD_BUTTON_XPATH)

    def comparing_text(self):
        time.sleep(3)
        self.assert_element_text(self.driver, self.EXPECTED_VALIDATION_INFO_XPATH, self.EXPECTED_VALIDATION_INFO)

    # def assert_element_text(self, driver, xpath, expected_text):
    #     element = driver.find_element(by=By.XPATH, xpath=self.expected_validation_info_xpath)
    #     expected_validation_info = element.text
    #     assert expected_text == expected_validation_info

        # def assert_element_text(self, driver, xpath, expected_text):
        #     """Comparing expected text with observed value from web element
        #
        #         :param driver: webdriver instance
        #         :param xpath: xpath to element with text to be observed
        #         :param expected_text: text what we expecting to be found
        #         :return: None
        #     """
        #     element = driver.find_element(by=By.XPATH, value=xpath)
        #     element_text = element.text
        #     assert expected_text == element_text
