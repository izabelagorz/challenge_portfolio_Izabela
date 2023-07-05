from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*@id='login']"
    button_main_page_xpath = "// div / span[text() = 'Main page']"
    button_players_xpath = "// div / span[text() = 'Players']"
    button_language_xpath = 