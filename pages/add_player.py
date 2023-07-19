import time

from pages.base_page import BasePage


class AddaPlayer(BasePage):
    login_url = "https://scouts.futbolkolektyw.pl/en/"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()= 'Sign in']"
    add_player_button_xpath = "//*[text()='Add player']"
    expected_add_player_title = "Add player"



    player_form_url = "https://scouts.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    main_page_button_xpath = "//div/span[text()='Main page']"
    add_player = "//button/span[text()='Add player']"
    expected_text_xpath = "//*[text()='Add player']"
    email_field_add_player_xpath = "//div/input[1]"
    name_field_xpath = "//div/input[@name='name']"
    surname_field_xpath = "//div/input[@name='surname']"
    phone_field_xpath = "//div/input[@name='phone']"
    weight_field_xpath = "//div/input[@name='weight']"
    height_field_xpath = "//div/input[@name='height']"
    age_field_xpath = "//div/input[@name='age']"
    club_xpath = "//div/input[@name='club']"
    level_xpath = "//div/input[@name='level']"
    level_text_xpath = "//*[text()='Level']"
    main_position_xpath = "//div/input[@name='mainPosition']"
    second_position_xpath = "//div/input[@name='secondPosition']"
    achievements_xpath = "//div/input[@name='achievements']"
    laczy_nas_pilka_xpath = "//*[@name='webLaczy']"
    minut_xpath = "//div/input[@name='web90']"
    facebook_xpath = "//div/input[@name='webFB']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[1]"
    left_leg_xpath = "//li[2]"
    district_dropdown_xpath = "//*[@id='mui-component-select-district']"
    lower_silesia_xpath = "//*[@data-value='dolnoslaskie']"
    kuyavia_pomerania_xpath = "//*[@data-value='kujawsko-pomorskie']"
    lublin_xpath = "//*[@data-value='lubelskie']"
    lubusz_xpath = "//*[@data-value='lubuskie']"
    lodz_xpath = "//*[@data-value='lodzkie']"
    lesser_poland_xpath = "//*[@data-value='malopolskie']"
    masovia_xpath = "//*[@data-value='mazowieckie']"
    opole_xpath = "//*[@data-value='opolskie']"
    subcarpatia_xpath = "//*[@data-value='podkarpackie']"
    podlaskie_xpath = "//*[@data-value='podlaskie']"
    pomerania_xpath = "//*[@data-value='pomorskie']"
    submit_xpath = "//*[@type='submit']"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    clear_text_button_xpath = "//span[text()='Clear']"
    required_text_xpath = "//div/p[text()='Required']"



    def type_in_email(self, email):
        time.sleep(5)
        self.field_send_keys(self.email_field_add_player_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def click_on_the_sing_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_add_player_title

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_club(self, club):
        self.field_send_keys(self.club_xpath, club)

    def select_leg(self, leg):
        self.wait_for_element_to_be_clickable(self.leg_dropdown_xpath)
        self.click_on_the_element(self.leg_dropdown_xpath)
        if leg == "Right leg":
            self.wait_for_element_to_be_clickable(self.right_leg_xpath)
            self.click_on_the_element(self.right_leg_xpath)
        else:
            self.wait_for_element_to_be_clickable(self.left_leg_xpath)
            self.click_on_the_element(self.left_leg_xpath)

    def type_in_level(self, level):
        self.field_send_keys(self.level_xpath, level)

    def type_in_main_position(self, main):
        self.field_send_keys(self.main_position_xpath, main)

    def type_in_second_position(self, second):
        self.field_send_keys(self.second_position_xpath, second)

    def select_district(self, district):
        if district == "Lower Silesia":
            self.click_on_the_element(self.lower_silesia_xpath)
        elif district == "Kuyavia-Pomerania":
            self.click_on_the_element(self.kuyavia_pomerania_xpath)
        elif district == "Lublin":
            self.click_on_the_element(self.lublin_xpath)
        elif district == "Lubusz":
            self.click_on_the_element(self.lubusz_xpath)
        elif district == "Łódź":
            self.click_on_the_element(self.lodz_xpath)
        elif district == "Lesser Poland":
            self.click_on_the_element(self.lesser_poland_xpath)
        elif district == "Masovia":
            self.click_on_the_element(self.masovia_xpath)
        elif district == "Opole":
            self.click_on_the_element(self.opole_xpath)
        elif district == "Subcarpatia":
            self.click_on_the_element(self.subcarpatia_xpath)
        elif district == "Podlaskie":
            self.click_on_the_element(self.podlaskie_xpath)
        elif district == "Pomerania":
            self.click_on_the_element(self.pomerania_xpath)
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
        self.field_send_keys(self.achievements_xpath, achievements)

    def type_in_laczy_nas_pilka(self, laczy_nas_pilka):
        self.field_send_keys(self.laczy_nas_pilka_xpath, laczy_nas_pilka)

    def type_in_minut(self, minut):
        self.field_send_keys(self.minut_xpath, minut)

    def type_in_facebook(self, facebook):
        self.field_send_keys(self.facebook_xpath, facebook)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_xpath)

    def click_on_the_main_page_button(self):
        self.click_on_the_element(self.main_page_button_xpath)

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def check_page_title(self):
        time.sleep(5)
        assert self.get_page_title() == self.expected_title

