import time

from pages.base_page import BasePage

"""LOKATORY"""
class AddaPlayer(BasePage):
    LOGIN_URL = "https://dareit.futbolkolektyw.pl/en"
    LOGIN_FIELD_XPATH = "//*[@id='login']"
    PASSWORD_FIELD_XPATH = "//*[@id='password']"
    SING_IN_BUTTON_XPATH = "//*[text()= 'Sign in']"
    ADD_PLAYER_BUTTON_XPATH = "//*[text()='Add player']"
    EXPECTED_ADD_PLAYER_TITLE = "Add player"



    PLAYER_FORM_URL = "https://dareit.futbolkolektyw.pl/en/players/add"
    EXPECTED_TITLE = "Add player"
    MAIN_PAGE_BUTTON_XPATH = "//div/span[text()='Main page']"
    ADD_PLAYER = "//button/span[text()='Add player']"
    EXPECTED_TEXT_XPATH = "//*[text()='Add player']"
    EMAIL_FIELD_ADD_PLAYER_XPATH = "//div/input[1]"
    NAME_FIELD_XPATH = "//div/input[@name='name']"
    SURNAME_FIELD_XPATH = "//div/input[@name='surname']"
    PHONE_FIELD_XPATH = "//div/input[@name='phone']"
    WEIGHT_FIELD_XPATH = "//div/input[@name='weight']"
    HEIGHT_FIELD_XPATH = "//div/input[@name='height']"
    AGE_FIELD_XPATH = "//div/input[@name='age']"
    CLUB_XPATH = "//div/input[@name='club']"
    LEVEL_XPATH = "//div/input[@name='level']"
    LEVEL_TEXT_XPATH = "//*[text()='Level']"
    MAIN_POSITION_XPATH = "//div/input[@name='mainPosition']"
    SECOND_POSITION_XPATH = "//div/input[@name='secondPosition']"
    ACHIEVEMENTS_XPATH = "//div/input[@name='achievements']"
    LACZY_NAS_PILKA_XPATH = "//*[@name='webLaczy']"
    MINUT_XPATH = "//div/input[@name='web90']"
    FACEBOOK_XPATH = "//div/input[@name='webFB']"
    LEG_DROPDOWN_XPATH = "//*[@id='mui-component-select-leg']"
    RIGHT_LEG_XPATH = "//li[1]"
    LEFT_LEG_XPATH = "//li[2]"
    DISTRICT_DROPDOWN_XPATH = "//*[@id='mui-component-select-district']"
    LOWER_SILESIA_XPATH = "//*[@data-value='dolnoslaskie']"
    KUYAVIA_POMERANIA_XPATH = "//*[@data-value='kujawsko-pomorskie']"
    LUBLIN_XPATH = "//*[@data-value='lubelskie']"
    LUBUSZ_XPATH = "//*[@data-value='lubuskie']"
    LODZ_XPATH = "//*[@data-value='lodzkie']"
    LESSER_POLAND_XPATH = "//*[@data-value='malopolskie']"
    MASOVIA_XPATH = "//*[@data-value='mazowieckie']"
    OPOLE_XPATH = "//*[@data-value='opolskie']"
    SUBCARPATIA_XPATH = "//*[@data-value='podkarpackie']"
    PODLASKIE_XPATH = "//*[@data-value='podlaskie']"
    POMERANIA_XPATH = "//*[@data-value='pomorskie']"
    SUBMIT_XPATH = "//*[@type='submit']"
    CLEAR_BUTTON_XPATH = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    CLEAR_TEXT_BUTTON_XPATH = "//span[text()='Clear']"
    REQUIRED_TEXT_XPATH = "//div/p[text()='Required']"



    def type_in_email(self, email):
        time.sleep(5)
        self.field_send_keys(self.EMAIL_FIELD_ADD_PLAYER_XPATH, email)

    def type_in_name(self, name):
        self.field_send_keys(self.NAME_FIELD_XPATH, name)

    def click_on_the_sing_in_button(self):
        self.click_on_the_element(self.SING_IN_BUTTON_XPATH)

    def click_on_add_player_button(self):
        self.click_on_the_element(self.ADD_PLAYER_BUTTON_XPATH)

    def title_of_page(self):
        assert self.get_page_title(self.LOGIN_URL) == self.EXPECTED_ADD_PLAYER_TITLE

    def type_in_surname(self, surname):
        self.field_send_keys(self.SURNAME_FIELD_XPATH, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.PHONE_FIELD_XPATH, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.WEIGHT_FIELD_XPATH, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.HEIGHT_FIELD_XPATH, height)

    def type_in_age(self, age):
        self.field_send_keys(self.AGE_FIELD_XPATH, age)

    def type_in_club(self, club):
        self.field_send_keys(self.CLUB_XPATH, club)

    def select_leg(self, leg):
        self.wait_for_element_to_be_clickable(self.LEG_DROPDOWN_XPATH)
        self.click_on_the_element(self.LEG_DROPDOWN_XPATH)
        if leg == "Right leg":
            self.wait_for_element_to_be_clickable(self.RIGHT_LEG_XPATH)
            self.click_on_the_element(self.RIGHT_LEG_XPATH)
        else:
            self.wait_for_element_to_be_clickable(self.LEFT_LEG_XPATH)
            self.click_on_the_element(self.LEFT_LEG_XPATH)

    def type_in_level(self, level):
        self.field_send_keys(self.LEVEL_XPATH, level)

    def type_in_main_position(self, main):
        self.field_send_keys(self.MAIN_POSITION_XPATH, main)

    def type_in_second_position(self, second):
        self.field_send_keys(self.SECOND_POSITION_XPATH, second)

    def select_district(self, district):
        if district == "Lower Silesia":
            self.click_on_the_element(self.LOWER_SILESIA_XPATH)
        elif district == "Kuyavia-Pomerania":
            self.click_on_the_element(self.KUYAVIA_POMERANIA_XPATH)
        elif district == "Lublin":
            self.click_on_the_element(self.LUBLIN_XPATH)
        elif district == "Lubusz":
            self.click_on_the_element(self.LUBUSZ_XPATH)
        elif district == "Łódź":
            self.click_on_the_element(self.LODZ_XPATH)
        elif district == "Lesser Poland":
            self.click_on_the_element(self.LESSER_POLAND_XPATH)
        elif district == "Masovia":
            self.click_on_the_element(self.MASOVIA_XPATH)
        elif district == "Opole":
            self.click_on_the_element(self.OPOLE_XPATH)
        elif district == "Subcarpatia":
            self.click_on_the_element(self.SUBCARPATIA_XPATH)
        elif district == "Podlaskie":
            self.click_on_the_element(self.PODLASKIE_XPATH)
        elif district == "Pomerania":
            self.click_on_the_element(self.POMERANIA_XPATH)
        elif district == "Silesia":
            self.click_on_the_element(self.silesia_xpath)
        elif district == "Holly Cross Province":
            self.click_on_the_element(self.holly_cross_province_xpath)
        elif district == "Warmia Masuria":
            self.click_on_the_element(self.warmia_masuria_xpath)
        elif district == "Greater Poland":
            self.click_on_the_element(self.greater_poland_xpath)
        else:
            self.click_on_the_element(self.west_pomerania_xpath)
    def type_in_achievements(self, achievements):
        self.field_send_keys(self.ACHIEVEMENTS_XPATH, achievements)

    def type_in_laczy_nas_pilka(self, laczy_nas_pilka):
        self.field_send_keys(self.LACZY_NAS_PILKA_XPATH, laczy_nas_pilka)

    def type_in_minut(self, minut):
        self.field_send_keys(self.MINUT_XPATH, minut)

    def type_in_facebook(self, facebook):
        self.field_send_keys(self.FACEBOOK_XPATH, facebook)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.ADD_PLAYER_BUTTON_XPATH)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.SING_IN_BUTTON_XPATH)

    def click_submit_button(self):
        self.click_on_the_element(self.SUBMIT_XPATH)

    def click_on_the_main_page_button(self):
        self.click_on_the_element(self.MAIN_PAGE_BUTTON_XPATH)

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.CLEAR_BUTTON_XPATH)

    def check_page_title(self):
        time.sleep(5)
        assert self.get_page_title() == self.EXPECTED_TITLE

