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
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    add_player = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    expected_text_xpath = "//*[text()='Add player']"
    email_field_add_player_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    name_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    phone_text_xpath = "//*[text()='Phone']"
    phone_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    weight_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    height_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/div/div/input"
    age_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    club_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    level_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    main_position_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    second_position_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    achievements_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[14]/div/div/input"
    laczy_nas_pilka_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[16]/div/div/input"
    minut_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[17]/div/div/input"
    facebook_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[18]/div/div/input"
    level_text_xpath = "//*[text()='Level']"
    right_leg_dropdown_xpath = "// *[ @ id = 'menu-leg'] / div[3] / ul / li[1]"
    leg_field_xpath = "//*[@id='mui-component-select-leg']"
    left_leg_dropdown_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    district_dropdown_xpath = "//*[@id='mui-component-select-district']"
    lower_silesia_xpath = "//*[@id='menu-district']/div[3]/ul/li[1]"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    clear_text_button_xpath = "//*[text()='Clear']"
    required_text_xpath = "//*[text()='Required']"


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


    #
    # def type_in_surname(self, surname):
    #     self.field_send_keys(self.surname_field_xpath, surname)
    #
    # def type_in_phone(self, phone):
    #     self.field_send_keys(self.phone_field_xpath, phone)
    #
    # def type_in_weight(self, weight):
    #     self.field_send_keys(self.weight_field_xpath, weight)
    #
    # def type_in_height(self, height):
    #     self.field_send_keys(self.height_field_xpath, height)
    #
    # def type_in_age(self, age):
    #     self.field_send_keys(self.age_field_xpath, age)
    #
    # def type_in_club(self, club):
    #     self.field_send_keys(self.club_xpath, club)
    #
    # def click_on_the_leg(self):
    #     self.click_on_the_element(self.leg_field_xpath)
    #
    # def click_on_the_right_leg(self):
    #     time.sleep(5)
    #     self.click_on_the_element(self.right_leg_dropdown_xpath)
    #
    # def type_in_level(self, level):
    #     self.field_send_keys(self.level_xpath, level)
    #
    # def type_in_main_position(self, main):
    #     self.field_send_keys(self.main_position_xpath, main)
    #
    # def type_in_second_position(self, second):
    #     self.field_send_keys(self.second_position_xpath, second)
    #
    # def click_on_the_district(self):
    #     self.click_on_the_element(self.district_dropdown_xpath)
    #
    # def click_on_the_lower_silesia(self):
    #     time.sleep(5)
    #     self.click_on_the_element(self.lower_silesia_xpath)
    #
    # def type_in_achievements(self, achievements):
    #     self.field_send_keys(self.achievements_xpath, achievements)
    #
    # def type_in_laczy_nas_pilka(self, pilka):
    #     self.field_send_keys(self.laczy_nas_pilka_xpath, pilka)
    #
    # def type_in_minut(self, minut):
    #     self.field_send_keys(self.minut_xpath, minut)
    #
    # def type_in_facebook(self, facebook):
    #     self.field_send_keys(self.facebook_xpath, facebook)
    #
    # def click_on_the_add_player_button(self):
    #     self.click_on_the_element(self.add_player_button_xpath)
    #
    # def click_on_the_sign_in_button(self):
    #     self.click_on_the_element(self.sign_in_button_xpath)
    #
    # def click_on_the_submit_button(self):
    #     self.click_on_the_element(self.submit_button_xpath)
    #
    # def click_on_the_main_page_button(self):
    #     self.click_on_the_element(self.main_page_button_xpath)
    #
    # def click_on_the_clear_button(self):
    #     self.click_on_the_element(self.clear_button_xpath)

