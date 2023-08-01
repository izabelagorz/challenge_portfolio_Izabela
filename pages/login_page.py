import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = 'https://dareit.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/from/div/div[1]/h5"
    header_of_box = 'Scouts Panel'
    sign_out_button_xpath = "//div/span[text()='Logout']"
    change_language_button_xpath = "//div/span[text()='Polski']"
    expected_validation_info = "Identifier or password invalid."
    expected_validation_info_xpath = "//span[text()='Identifier or password invalid.']"
    remind_password_button_xpath = "//div/a[text()='Remind password']"
    remind_email_field_xpath = "//input"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_remind_email(self, email):
        self.field_send_keys(self.remind_email_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sing_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_send_button(self):
        self.click_on_the_element(self.remind_email_field_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def click_on_the_sing_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_on_change_language_button(self):
        self.click_on_the_element(self.change_language_button_xpath)

    def click_on_remind_password_button(self):
        self.click_on_the_element(self.remind_password_button_xpath)

    def comparing_text(self):
        time.sleep(3)
        self.assert_element_text(self.driver, self.expected_validation_info_xpath, self.expected_validation_info)

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
