from pages.base_page import BasePage
from locators.hymn_page_locators import HymnPageLocators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from pages.components.menu_component import MenuComponent


class HymnPage(MenuComponent):

    def get_title(self):
        return self.get_text(HymnPageLocators.TITLE)

    def open_previous_hymn(self):
        self.click(HymnPageLocators.PREVIOUS_HYMN_BUTTON)

    def open_next_hymn(self):
        self.click(HymnPageLocators.NEXT_HYMN_BUTTON)

    def toggle_favorite(self):
        self.click(HymnPageLocators.FAVORITE_BUTTON)

    def play_hymn(self):
        self.click(HymnPageLocators.PLAY_BUTTON)

    def add_to_list(self):
        self.click(HymnPageLocators.ADD_TO_LIST_BUTTON)
        return self

    def mark_as_known(self):
        self.click(HymnPageLocators.KNOWN_BUTTON)

    def rewind(self):
        self.click(HymnPageLocators.REWIND_BUTTON)

    def play_pause(self):
        self.click(HymnPageLocators.PLAY_PAUSE_BUTTON)

    def forward(self):
        self.click(HymnPageLocators.FORWARD_BUTTON)

    def get_current_playback_time(self):
        return self.get_text(HymnPageLocators.CURRENT_TIME)

    def get_total_playback_duration(self):
        return self.get_text(HymnPageLocators.DURATION_TIME)

    def is_music_player_displayed(self):
        return self.is_displayed(HymnPageLocators.MUSIC_PLAYER_CONTAINER)

    def get_verse_texts(self):
        elements = self.driver.find_elements(*HymnPageLocators.VERSE_TEXTS)
        return [element.text for element in elements]

    def is_add_to_list_popup_displayed(self):
        """Check if the add to list popup is displayed"""
        return self.is_displayed(HymnPageLocators.POPUP_LIST_NAME_TEXT)

    def get_popup_title(self):
        """Get the title of the add to list popup"""
        return self.get_text(HymnPageLocators.POPUP_TITLE)

    def select_list_from_popup(self, list_name):
        """Select a specific list from the popup by name"""
        list_name_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='com.pentecostal.himnarioprincipal:id/name_record_pop' and @text='{list_name}']"
        )
        self.click(list_name_locator)
        return self

    def close_popup(self):
        """Close the add to list popup"""
        self.click(HymnPageLocators.POPUP_CLOSE_BUTTON)
        return self
