from pages.base_page import BasePage
from locators.classification_locators import ClassificationLocators


class ClassificationPage(BasePage):

    def get_title(self):
        return self.get_text(ClassificationLocators.TITLE)

    def open_category(self, category_text):
        category_locator = ClassificationLocators.category_item(category_text)
        try:
            self.click(category_locator)
        except Exception:
            scroll_locator = ClassificationLocators.category_item_scrollable(category_text)
            self.click(scroll_locator)

    def is_category_displayed(self, category_text):
        return self.is_displayed(ClassificationLocators.category_item(category_text))
