from pages.base_page import BasePage
from locators.components.menu_locator import MenuLocators


class MenuComponent(BasePage):

    def open_drawer(self):
        self.click(MenuLocators.DRAWER_BUTTON)

    def click_home_button(self):
        self.click(MenuLocators.HOME_BUTTON_BAR)

    def open_settings(self):
        self.open_drawer()
        self.click(MenuLocators.SETTINGS_ITEM)
        from pages.settings_page import SettingsPage
        return SettingsPage(self.driver)
