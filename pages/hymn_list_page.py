from appium.webdriver.common.appiumby import AppiumBy
from pages.components.menu_component import MenuComponent
from pages.hymn_page import HymnPage
from locators.hymn_list_locators import HymnListLocators


class HymnListPage(MenuComponent):

    def get_all_hymn_names(self):
        """Get all hymn titles/names from the list"""
        hymn_elements = self.driver.find_elements(*HymnListLocators.HYMN_TITLE)
        return [element.text for element in hymn_elements]

    def open_hymn_by_title(self, title):
        hymn_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{HymnListLocators.HYMN_TITLE[1]}' and @text='{title}']"
        )
        self.click(hymn_locator)
        return HymnPage(self.driver)

    def open_hymn_by_number(self, number):
        number_text = f"{number}.- "
        hymn_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{HymnListLocators.HYMN_NUMBER[1]}' and @text='{number_text}']/.."
        )
        self.click(hymn_locator)
        return HymnPage(self.driver)

    def is_music_icon_displayed(self) -> bool:
        """Check if at least one music note icon is displayed in the list."""
        return self.is_displayed(HymnListLocators.MUSIC_ICON)

    def are_music_icons_present(self) -> bool:
        """Return True if music note icons are currently found in the view."""
        elements = self.driver.find_elements(*HymnListLocators.MUSIC_ICON)
        return len(elements) > 0

    def get_first_hymn_title_height(self) -> int:
        """Get the pixel height of the first hymn title record."""
        element = self.find_element(HymnListLocators.HYMN_TITLE)
        return element.size.get("height", 0)
