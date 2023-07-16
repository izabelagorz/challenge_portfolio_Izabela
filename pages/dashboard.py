import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*@id='login']"
    button_main_page_xpath = "//div/span[text() = 'Strona główna' or text() ='Main page']"
    button_players_xpath = "//div/span[text() = 'Gracze' or text() ='Players']"
    button_language_xpath = "//div/span[text() = 'Polski' or text() ='English']"
    button_sign_out_xpath = "//div/span[text() = 'Wyloguj' or text() ='Sing out']"
    button_add_player_xpath = "//button/span[text()='Add player' or text()='Dodaj gracza']"
    last_created_player_xpath = "//h6[text()='Last created player']/following-sibling::a"
    last_created_match_xpath = "//h6[text()='Last created match']/following-sibling::a"
    last_updated_player_xpath = "//h6[text()='Last updated player']/following-sibling::a"
    last_updated_match_xpath = "//h6[text()='Last updated match']/following-sibling::a"
    last_updated_report_xpath = "//h6[text()='Last updated report']/following-sibling::a"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    futbol_kolektyw_button_xpath = '//*[@title="Logo Scouts Panel"]'
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)
