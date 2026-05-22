from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.hymn_page import HymnPage
from pages.home_page import HomePage
from locators.favoritos_locators import FavoritosLocators


class FavoritosPage(BasePage):

    def get_title(self):
        """Get the title of the Favoritos page"""
        return self.get_text(FavoritosLocators.TITLE)

    def open_hymn_by_title(self, title):
        """Open a hymn from favorites by its title"""
        hymn_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{FavoritosLocators.HYMN_TITLE[1]}' and @text='{title}']"
        )
        self.click(hymn_locator)
        return HymnPage(self.driver)

    def open_hymn_by_number(self, number):
        """Open a hymn from favorites by its number"""
        number_text = f"{number}.- "
        hymn_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{FavoritosLocators.HYMN_NUMBER[1]}' and @text='{number_text}']/.."
        )
        self.click(hymn_locator)
        return HymnPage(self.driver)

    def go_to_home(self):
        """Navigate back to home page"""
        self.click(FavoritosLocators.HOME_BUTTON)
        return HomePage(self.driver)

    def open_navigation_drawer(self):
        """Open the navigation drawer menu"""
        self.click(FavoritosLocators.NAVIGATION_DRAWER)
