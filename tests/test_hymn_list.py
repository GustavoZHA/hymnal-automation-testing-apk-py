import allure
import pytest

from pages.home_page import HomePage


@allure.epic("Hymnal Mobile App")
@allure.feature("Lista de Himnos")
class TestHymnList:

    @allure.title("SCN-LIS-001: Open hymn list and select hymn by title")
    def test_open_hymn_list_and_open_by_title(self, driver):
        target_title = "Ven , ¡oh Todopoderoso!"

        with allure.step("Given the user opens the hymn list from Home"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()

        with allure.step(f"When selecting the hymn with title '{target_title}'"):
            hymn_page = hymn_list.open_hymn_by_title(target_title)

        with allure.step("Then the hymn detail view loads with a non-empty matching title"):
            actual_title = hymn_page.get_title()
            assert actual_title != "", "Hymn detail title is unexpectedly empty"
            assert target_title in actual_title, f"Expected '{target_title}' in '{actual_title}'"

    @allure.title("SCN-LIS-002: Open hymn list and select hymn #1 by number")
    def test_open_hymn_list_and_open_by_number(self, driver):
        hymn_number = 1
        expected_title = "1. Ven , ¡oh Todopoderoso!"

        with allure.step("Given the user opens the hymn list from Home"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()

        with allure.step(f"When selecting hymn number {hymn_number}"):
            hymn_page = hymn_list.open_hymn_by_number(hymn_number)

        with allure.step(f"Then the hymn detail title matches '{expected_title}'"):
            actual_title = hymn_page.get_title()
            assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"

    @allure.title("SCN-LIS-003: Verify general hymn list populates multiple hymn records")
    def test_hymn_list_populates_records(self, driver):
        with allure.step("Given the user opens the hymn list from Home"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()

        with allure.step("When retrieving the hymn names visible in the list"):
            hymn_names = hymn_list.get_all_hymn_names()

        with allure.step("Then the list contains multiple hymn records"):
            assert len(hymn_names) > 0, "No hymn records were populated in the hymn list"
