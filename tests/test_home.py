import allure
import pytest

from pages.home_page import HomePage
from pages.hymn_list_page import HymnListPage
from pages.hymn_page import HymnPage


@allure.epic("Hymnal Mobile App")
@allure.feature("Home")
class TestHome:

    @allure.title("SCN-HOM-001: Open hymn list from the Home main button")
    def test_open_hymnal(self, driver):
        with allure.step("Given the user is on the main Home screen"):
            home = HomePage(driver)

        with allure.step("When clicking the 'Himnario' button"):
            hymn_list = home.open_hymnal()

        with allure.step("Then the hymn list screen is displayed"):
            assert isinstance(hymn_list, HymnListPage), "Navigation to HymnListPage failed"

    @allure.title("SCN-HOM-002: Navigate from Home to list and open hymn by title")
    def test_open_hymn_by_title(self, driver):
        target_title = "Ven , ¡oh Todopoderoso!"

        with allure.step("Given the user opens the general hymn list from Home"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()

        with allure.step(f"When selecting the hymn '{target_title}'"):
            hymn_page = hymn_list.open_hymn_by_title(target_title)

        with allure.step(f"Then the hymn detail view opens with title containing '{target_title}'"):
            actual_title = hymn_page.get_title()
            assert target_title in actual_title, f"Expected '{target_title}' in hymn title, but got: '{actual_title}'"
            assert isinstance(hymn_page, HymnPage), "Expected instance of HymnPage"
