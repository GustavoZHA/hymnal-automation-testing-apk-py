from pages.base_page import BasePage
from locators.components.menu_locator import MenuLocators

class MenuComponent(BasePage):

    def open_drawer(self):
        self.click(MenuLocators.DRAWER_BUTTON)

    def click_home_button(self):
        self.click(MenuLocators.HOME_BUTTON_BAR)
