from pages.base_page import BasePage
from locators.home_locators import HomeLocators
from pages.hymn_list_page import HymnListPage
from pages.classification_page import ClassificationPage
from pages.search_page import SearchPage


class HomePage(BasePage):

    def open_hymnal(self):
        self.click(HomeLocators.HYMNAL_BUTTON)
        return HymnListPage(self.driver)

    def open_search(self):
        self.click(HomeLocators.SEARCH_BUTTON)
        return SearchPage(self.driver)

    def open_favorites(self):
        self.click(HomeLocators.FAVORITES_BUTTON)

    def open_known(self):
        self.click(HomeLocators.KNOWN_BUTTON)

    def open_classification(self):
        self.click(HomeLocators.CLASSIFICATION_BUTTON)
        return ClassificationPage(self.driver)

    def open_personalized_lists(self):
        self.click(HomeLocators.PERSONALIZED_LISTS_BUTTON)

    def get_title(self):
        return self.get_text(HomeLocators.TITLE)
