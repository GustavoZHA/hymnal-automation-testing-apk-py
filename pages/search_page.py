from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.hymn_page import HymnPage
from locators.search_locators import SearchLocators


class SearchPage(BasePage):

    def enter_search_query(self, query):
        field = self.wait.until(EC.visibility_of_element_located(SearchLocators.SEARCH_INPUT))
        field.clear()
        field.send_keys(query)
        return self

    def submit_search(self):
        self.click(SearchLocators.SEARCH_BUTTON)
        return self

    def search_hymn(self, query):
        self.enter_search_query(query)
        self.submit_search()
        return self

    def get_result_items(self):
        return self.wait.until(EC.presence_of_all_elements_located(SearchLocators.RESULT_ITEM))

    def get_results_count(self):
        return len(self.get_result_items())

    def open_hymn_by_title(self, title):
        hymn_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{SearchLocators.RESULT_TITLE[1]}' and @text='{title}']"
        )
        self.click(hymn_locator)
        return HymnPage(self.driver)

    def open_hymn_by_number(self, number):
        number_text = f"{number}.- "
        hymn_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{SearchLocators.RESULT_NUMBER[1]}' and @text='{number_text}']/.."
        )
        self.click(hymn_locator)
        return HymnPage(self.driver)

    def get_toast_message(self):
        return self.wait.until(EC.presence_of_element_located(SearchLocators.TOAST_MESSAGE)).text
