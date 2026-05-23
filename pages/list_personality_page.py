from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.list_personality_locators import ListPersonalityLocators
from pages.components.menu_component import MenuComponent


class ListPersonalityPage(MenuComponent):

    def is_page_displayed(self):
        """Verify if the List Personality page is displayed"""
        return self.is_displayed(ListPersonalityLocators.TITLE)

    def get_page_title(self):
        """Get the page title text"""
        title_element = self.wait.until(EC.visibility_of_element_located(ListPersonalityLocators.TITLE))
        return title_element.text

    def enter_list_name(self, name):
        """Enter name for new list in the input field"""
        field = self.wait.until(EC.visibility_of_element_located(ListPersonalityLocators.NAME_INPUT))
        field.clear()
        field.send_keys(name)
        return self

    def click_create_button(self):
        """Click the create button to create a new list"""
        self.click(ListPersonalityLocators.CREATE_BUTTON)
        return self

    def create_new_list(self, list_name):
        """Create a new personalized list"""
        self.enter_list_name(list_name)
        self.click_create_button()
        return self

    def get_all_lists(self):
        """Get all list records"""
        return self.wait.until(EC.presence_of_all_elements_located(ListPersonalityLocators.LIST_RECORD_ITEM))

    def get_lists_count(self):
        """Get the count of lists"""
        return len(self.get_all_lists())

    def get_list_names(self):
        """Get all list names as text"""
        list_items = self.get_all_lists()
        names = []
        for item in list_items:
            name_element = item.find_element(*ListPersonalityLocators.LIST_NAME_TEXT)
            names.append(name_element.text)
        return names

    def click_list_by_name(self, list_name):
        """Click on a specific list by its name"""
        list_name_locator = (
            AppiumBy.XPATH,
            f"//android.widget.TextView[@resource-id='{ListPersonalityLocators.LIST_NAME_TEXT[1]}' and @text='{list_name}']"
        )
        self.click(list_name_locator)
        return self

    def delete_list_by_name(self, list_name):
        """Delete a specific list by clicking the delete button associated with it"""
        # Find the record item containing the list name and then find the delete button within it
        list_record_xpath = f"//android.widget.LinearLayout[@resource-id='{ListPersonalityLocators.LIST_RECORD_ITEM[1]}' and .//android.widget.TextView[@text='{list_name}']]"
        list_record = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, list_record_xpath)))
        
        # Find the delete button within this record
        delete_button = list_record.find_element(*ListPersonalityLocators.DELETE_LIST_BUTTON)
        delete_button.click()
        return self

    def is_list_name_visible(self, list_name):
        """Check if a specific list name is visible"""
        try:
            list_name_locator = (
                AppiumBy.XPATH,
                f"//android.widget.TextView[@resource-id='{ListPersonalityLocators.LIST_NAME_TEXT[1]}' and @text='{list_name}']"
            )
            self.wait.until(EC.visibility_of_element_located(list_name_locator), timeout=5)
            return True
        except:
            return False

    def is_name_input_visible(self):
        """Verify if the name input field is visible"""
        return self.is_displayed(ListPersonalityLocators.NAME_INPUT)

    def get_name_input_hint(self):
        """Get the hint text from the name input field"""
        field = self.wait.until(EC.visibility_of_element_located(ListPersonalityLocators.NAME_INPUT))
        return field.get_attribute("hint")

    def clear_name_input(self):
        """Clear the name input field"""
        field = self.wait.until(EC.visibility_of_element_located(ListPersonalityLocators.NAME_INPUT))
        field.clear()
        return self
    
    def get_toast_message(self):
        return self.wait.until(EC.presence_of_element_located(ListPersonalityLocators.TOAST_MESSAGE)).text

