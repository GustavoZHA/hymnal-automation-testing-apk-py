from pages.base_page import BasePage
from locators.home_locators import HomeLocators


class HomePage(BasePage):

    def open_hymnal(self):
        self.click(HomeLocators.HYMNAL_BUTTON)

    def open_search(self):
        self.click(HomeLocators.SEARCH_BUTTON)

    def open_favorites(self):
        self.click(HomeLocators.FAVORITES_BUTTON)

    def open_classification(self):
        self.click(HomeLocators.CLASSIFICATION_BUTTON)
