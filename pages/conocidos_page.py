from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.hymn_page import HymnPage
from pages.home_page import HomePage
from locators.conocidos_locators import ConocidosLocators


class ConocidosPage(BasePage):

    def get_title(self):
        """Get the title of the Conocidos page"""
        return self.get_text(ConocidosLocators.TITLE)

    def open_hymn_by_title(self, title):
        """Open a hymn from conocidos by its title"""
        hymn_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{ConocidosLocators.HYMN_TITLE[1]}' and @text='{title}']"
        )
        self.click(hymn_locator)
        return HymnPage(self.driver)

    def open_hymn_by_number(self, number):
        """Open a hymn from conocidos by its number"""
        number_text = f"{number}.- "
        hymn_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{ConocidosLocators.HYMN_NUMBER[1]}' and @text='{number_text}']/.."
        )
        self.click(hymn_locator)
        return HymnPage(self.driver)

    def go_to_home(self):
        """Navigate back to home page"""
        self.click(ConocidosLocators.HOME_BUTTON)
        return HomePage(self.driver)

    def open_navigation_drawer(self):
        """Open the navigation drawer menu"""
        self.click(ConocidosLocators.NAVIGATION_DRAWER)
