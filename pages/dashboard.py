import time

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    LOGIN_BUTTON_XPATH = "//*@id='login']"
    BUTTON_MAIN_PAGE_XPATH = "//div/span[text() = 'Strona główna' or text() ='Main page']"
    BUTTON_PLAYERS_XPATH = "//div/span[text() = 'Gracze' or text() ='Players']"
    BUTTON_LANGUAGE_XPATH = "//div/span[text() = 'Polski' or text() ='English']"
    BUTTON_SING_OUT_XPATH = "//div/span[text() = 'Wyloguj' or text() ='Sing out']"
    BUTTON_ADD_PLAYER_XPATH = "//button/span[text()='Add player' or text()='Dodaj gracza']"
    LAST_CREATED_PLAYER_XPATH = "//h6[text()='Last created player']/following-sibling::a"
    LAST_CREATED_MATCH_XPATH = "//h6[text()='Last created match']/following-sibling::a"
    LAST_UPDATED_PLAYER_XPATH = "//h6[text()='Last updated player']/following-sibling::a"
    LAST_UPDATED_MATCH_XPATH = "//h6[text()='Last updated match']/following-sibling::a"
    LAST_UPDATED_REPORT_XPATH = "//h6[text()='Last updated report']/following-sibling::a"
    ADD_PLAYER_BUTTON_XPATH = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    FOOTBALL_KOLEKTYW_BUTTON_XPATH = '//*[@title="Logo Scouts Panel"]'
    EXPECTED_TITLE = "Scouts panel"
    DASHBOARD_URL = "https://dareit.futbolkolektyw.pl/en"

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.FOOTBALL_KOLEKTYW_BUTTON_XPATH)
        assert self.get_page_title(self.DASHBOARD_URL) == self.EXPECTED_TITLE

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.ADD_PLAYER_BUTTON_XPATH)
