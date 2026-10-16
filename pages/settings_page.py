from pages.base_page import BasePage
from locators.settings_locators import SettingsLocators


class SettingsPage(BasePage):
    """Page Object for the Settings screen."""

    def toggle_theme(self):
        self.click(SettingsLocators.THEME_SWITCH)

    def increase_font(self):
        self.click(SettingsLocators.INCREASE_FONT_BUTTON)

    def decrease_font(self):
        self.click(SettingsLocators.DECREASE_FONT_BUTTON)

    def toggle_visible_music(self):
        self.click(SettingsLocators.VISIBLE_MUSIC_SWITCH)

    def is_settings_title_displayed(self) -> bool:
        return self.is_displayed(SettingsLocators.SETTINGS_TITLE)
