import pytest

from datetime import datetime

from pages.home_page import HomePage
from pages.hymn_list_page import HymnListPage
from pages.list_personality_page import ListPersonalityPage
from locators.list_personality_locators import ListPersonalityLocators


class TestListPersonality:

    def test_open_list_personality_page_and_verify_title(self, driver):
        """Test opening the list personality page and verifying the title"""
        home = HomePage(driver)
        list_personality = home.open_list_personality()

        assert list_personality.is_page_displayed()
        assert list_personality.get_page_title() == "Listas Personalizadas"

    def test_verify_list_personality_page_elements(self, driver):
        """Test that all main elements are displayed on the page"""
        home = HomePage(driver)
        list_personality = home.open_list_personality()

        assert list_personality.is_displayed(ListPersonalityLocators.NAME_INPUT)
        assert list_personality.is_displayed(ListPersonalityLocators.CREATE_BUTTON)
        assert list_personality.is_displayed(ListPersonalityLocators.LISTS_CONTAINER)

    def test_verify_name_input_hint_text(self, driver):
        """Test that the name input field has the correct hint text"""
        home = HomePage(driver)
        list_personality = home.open_list_personality()

        hint_text = list_personality.get_name_input_hint()
        assert hint_text == "Escriba el nombre de Lista a Crear"

    def test_clear_name_input_field(self, driver):
        """Test clearing the name input field"""
        home = HomePage(driver)
        list_personality = home.open_list_personality()

        list_personality.enter_list_name("Test Text")
        list_personality.clear_name_input()

        # Verify the field is empty
        field_text = list_personality.driver.find_element(*ListPersonalityLocators.NAME_INPUT).text
        assert field_text in "Escriba el nombre de Lista a Crear"

    def test_create_new_personalized_list(self, driver):
        """Test creating a new personalized list"""
        home = HomePage(driver)
        list_personality = home.open_list_personality()

        list_name = "CNL" + datetime.now().strftime("%H:%M:%S.%f")[:-3]
        list_personality.create_new_list(list_name)

        toast_text = list_personality.get_toast_message()
        assert "creada exitosamente" in toast_text

    def test_delete_personalized_list(self, driver):
        """Test deleting a personalized list"""
        self.test_create_new_personalized_list(driver)
        home = HomePage(driver)
        home.click_home_button()
        list_personality = home.open_list_personality()

        list_names = list_personality.get_list_names()
        list_to_delete = list_names[0]

        list_personality.delete_list_by_name(list_to_delete)

        assert not list_personality.is_list_name_visible(list_to_delete)

    def test_add_hymn_to_personalized_list(self, driver):
        """Test adding a hymn to a personalized list"""
        list_name = "TAL" + datetime.now().strftime("%H:%M:%S.%f")[:-3]
        hymn_title = "Cantemos aqui"

        # First, create a new list
        home = HomePage(driver)
        list_personality = home.open_list_personality()

        list_personality.create_new_list(list_name)

        # Wait for the toast message to confirm list creation
        toast_text = list_personality.get_toast_message()
        assert "creada exitosamente" in toast_text

        list_personality.click_home_button()
        # Navigate to hymn list and open a hymn
        home = HomePage(driver)
        hymn_list_page = home.open_hymnal()

        # Get first hymn and open it
        hymn = hymn_list_page.open_hymn_by_title(hymn_title)
        hymn.add_to_list()
        hymn.select_list_from_popup(list_name)
        hymn.click_home_button()

        home = HomePage(driver)
        list_personality = home.open_list_personality()
        list_personality.click_list_by_name(list_name)
        hymn_list_page = HymnListPage(driver)
        hymn_names = hymn_list_page.get_all_hymn_names()
        assert hymn_title in hymn_names, "Expected hymn was not found"
