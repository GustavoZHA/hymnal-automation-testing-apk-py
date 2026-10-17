from pages.components.menu_component import MenuComponent
from locators.settings_locators import SettingsLocators


class SettingsPage(MenuComponent):
    """Page Object representing the Settings (Configuraciones) screen."""

    def is_settings_title_displayed(self) -> bool:
        return self.is_displayed(SettingsLocators.SCREEN_CONFIG) or (
            self.is_displayed(SettingsLocators.TITLE) and "CONFIGURACION" in self.get_title().upper()
        )

    def get_title(self) -> str:
        return self.get_text(SettingsLocators.TITLE)

    def select_light_theme(self) -> "SettingsPage":
        self.click(SettingsLocators.MODE_LIGHT)
        return self

    def select_dark_theme(self) -> "SettingsPage":
        self.click(SettingsLocators.MODE_DARK)
        return self

    def increase_font(self) -> "SettingsPage":
        self.click(SettingsLocators.INCREASE_FONT_BUTTON)
        return self

    def decrease_font(self) -> "SettingsPage":
        self.click(SettingsLocators.DECREASE_FONT_BUTTON)
        return self

    def get_preview_text_height(self) -> int:
        element = self.find_element(SettingsLocators.PREVIEW_TEXT)
        return element.size.get("height", 0)

    def get_preview_verse_height(self) -> int:
        element = self.find_element(SettingsLocators.PREVIEW_VERSE)
        return element.size.get("height", 0)

    def is_music_switch_checked(self) -> bool:
        element = self.find_element(SettingsLocators.SWITCH_MUSIC)
        return element.get_attribute("checked") == "true"

    def toggle_visible_music(self) -> "SettingsPage":
        self.click(SettingsLocators.SWITCH_MUSIC)
        return self

    def set_music_switch(self, enable: bool) -> "SettingsPage":
        if self.is_music_switch_checked() != enable:
            self.toggle_visible_music()
        return self

    def click_export_backup(self) -> "SettingsPage":
        self.click(SettingsLocators.BTN_EXPORT_BACKUP)
        return self

    def is_export_dialog_displayed(self) -> bool:
        return self.is_displayed(SettingsLocators.EXPORT_DIALOG_TITLE)

    def get_export_dialog_title(self) -> str:
        return self.get_text(SettingsLocators.EXPORT_DIALOG_TITLE)

    def cancel_export_dialog(self) -> "SettingsPage":
        self.click(SettingsLocators.EXPORT_BTN_CANCEL)
        return self

    def click_import_backup(self) -> "SettingsPage":
        self.click(SettingsLocators.BTN_IMPORT_BACKUP)
        return self

    def select_backup_file(self, filename: str = "himnario_backup.json") -> "SettingsPage":
        file_locator = SettingsLocators.file_by_name(filename)
        self.click(file_locator)
        return self

    def return_to_home(self):
        self.click_home_button()
        from pages.home_page import HomePage
        return HomePage(self.driver)
