from datetime import datetime

import allure
import pytest

from pages.home_page import HomePage
from pages.hymn_list_page import HymnListPage
from pages.list_personality_page import ListPersonalityPage
from locators.list_personality_locators import ListPersonalityLocators


@allure.epic("Hymnal Mobile App")
@allure.feature("Listas Personalizadas")
class TestListPersonality:

    @allure.title("SCN-LST-001: Open Custom Playlists screen and verify title")
    def test_open_list_personality_page_and_verify_title(self, driver):
        with allure.step("Given the user is on the main Home screen"):
            home = HomePage(driver)

        with allure.step("When opening the Custom Playlists section"):
            list_personality = home.open_list_personality()

        with allure.step("Then the screen is displayed and title is 'Listas Personalizadas'"):
            assert list_personality.is_page_displayed(), "Custom Playlists screen is not displayed"
            actual_title = list_personality.get_page_title()
            assert actual_title == "Listas Personalizadas", (
                f"Expected page title 'Listas Personalizadas', but got '{actual_title}'"
            )

    @allure.title("SCN-LST-002: Verify main components on Custom Playlists screen")
    def test_verify_list_personality_page_elements(self, driver):
        with allure.step("Given the user accesses the Custom Playlists screen"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()

        with allure.step("Then the playlist name input and create button are visible"):
            assert list_personality.is_displayed(ListPersonalityLocators.NAME_INPUT), "Playlist name input not visible"
            assert list_personality.is_displayed(ListPersonalityLocators.CREATE_BUTTON), "Create playlist button not visible"

    @allure.title("SCN-LST-003: Verify hint text in playlist name input")
    def test_verify_name_input_hint_text(self, driver):
        with allure.step("Given the user accesses the Custom Playlists screen"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()

        with allure.step("When retrieving the hint placeholder of the name input field"):
            hint_text = list_personality.get_name_input_hint()

        with allure.step("Then the hint text must be 'Escriba el nombre de Lista a Crear'"):
            assert hint_text == "Escriba el nombre de Lista a Crear", (
                f"Expected hint 'Escriba el nombre de Lista a Crear', but got '{hint_text}'"
            )

    @allure.title("SCN-LST-004: Clear text in playlist name input")
    def test_clear_name_input_field(self, driver):
        with allure.step("Given the user enters text in the playlist name input"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()
            list_personality.enter_list_name("Test Text")

        with allure.step("When clearing the input field"):
            list_personality.clear_name_input()

        with allure.step("Then the input displays default hint or remains empty"):
            field_text = list_personality.driver.find_element(*ListPersonalityLocators.NAME_INPUT).text
            assert field_text in "Escriba el nombre de Lista a Crear", (
                f"Expected empty field or default placeholder, but found '{field_text}'"
            )

    @allure.title("SCN-LST-005: Create a new custom playlist successfully")
    def test_create_new_personalized_list(self, driver):
        list_name = "CNL" + datetime.now().strftime("%H:%M:%S.%f")[:-3]

        with allure.step("Given the user accesses the Custom Playlists screen"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()

        with allure.step(f"When typing list name '{list_name}' and clicking the create button"):
            list_personality.create_new_list(list_name)

        with allure.step("Then a confirmation Toast indicates successful creation"):
            toast_text = list_personality.get_toast_message()
            assert "creada exitosamente" in toast_text, (
                f"Expected Toast containing 'creada exitosamente', but got '{toast_text}'"
            )

    @allure.title("SCN-LST-006: Delete an existing custom playlist")
    def test_delete_personalized_list(self, driver):
        list_name = "CNL" + datetime.now().strftime("%H:%M:%S.%f")[:-3]

        with allure.step(f"Given a playlist named '{list_name}' is created"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()
            list_personality.create_new_list(list_name)
            toast = list_personality.get_toast_message()
            assert "creada exitosamente" in toast, f"Failed creating pre-condition list '{list_name}'"

        with allure.step("And the user returns Home and re-enters Custom Playlists"):
            home.click_home_button()
            list_personality = home.open_list_personality()

        with allure.step(f"When deleting the newly created playlist '{list_name}'"):
            list_personality.delete_list_by_name(list_name)

        with allure.step(f"Then playlist '{list_name}' is no longer visible in the list"):
            assert not list_personality.is_list_name_visible(list_name), (
                f"Playlist '{list_name}' is still visible after deletion"
            )

    @allure.title("SCN-LST-007: Add a hymn to a custom playlist and verify presence")
    def test_add_hymn_to_personalized_list(self, driver):
        list_name = "TAL" + datetime.now().strftime("%H:%M:%S.%f")[:-3]
        hymn_title = "Cantemos aqui"

        with allure.step(f"Given a new custom playlist '{list_name}' is created"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()
            list_personality.create_new_list(list_name)
            toast_text = list_personality.get_toast_message()
            assert "creada exitosamente" in toast_text, f"Failed creating pre-condition list '{list_name}'"

        with allure.step(f"When navigating to hymnal, opening hymn '{hymn_title}' and adding it to '{list_name}'"):
            list_personality.click_home_button()
            home = HomePage(driver)
            hymn_list_page = home.open_hymnal()
            hymn = hymn_list_page.open_hymn_by_title(hymn_title)
            hymn.add_to_list()
            hymn.select_list_from_popup(list_name)
            hymn.click_home_button()

        with allure.step(f"And opening custom playlist '{list_name}'"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()
            list_personality.click_list_by_name(list_name)

        with allure.step(f"Then hymn '{hymn_title}' is present in the playlist hymns"):
            hymn_list_page = HymnListPage(driver)
            hymn_names = hymn_list_page.get_all_hymn_names()
            assert hymn_title in hymn_names, f"Hymn '{hymn_title}' was not found in playlist '{list_name}'"
