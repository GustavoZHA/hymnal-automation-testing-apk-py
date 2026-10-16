import allure
import pytest

from pages.home_page import HomePage
from locators.search_locators import SearchLocators


@allure.epic("Hymnal Mobile App")
@allure.feature("Búsqueda de Himnos")
class TestSearchPage:

    @allure.title("SCN-BUS-001: Verify search screen elements presence")
    def test_open_search_page_and_verify_elements(self, driver):
        with allure.step("Given the user navigates to the search screen"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step("Then the search input and search button are visible"):
            assert search_page.is_displayed(SearchLocators.SEARCH_INPUT), "Search input field is not visible"
            assert search_page.is_displayed(SearchLocators.SEARCH_BUTTON), "Search button is not visible"

    @allure.title("SCN-BUS-002: Validate warning Toast when search text has fewer than 5 characters")
    def test_search_hymn_by_short_text_shows_validation_toast(self, driver):
        search_query = "des"

        with allure.step("Given the user is on the search screen"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"When searching with short text '{search_query}'"):
            search_page.search_hymn(search_query)

        with allure.step("Then the minimum length validation Toast is displayed"):
            toast_text = search_page.get_toast_message()
            assert toast_text == "El texto debe tener más de 5 caracteres", (
                f"Expected Toast 'El texto debe tener más de 5 caracteres', but got '{toast_text}'"
            )

    @allure.title("SCN-BUS-003: Validate warning Toast when hymn number is out of range")
    def test_search_hymn_by_number_out_of_range_shows_validation_toast(self, driver):
        number_out_of_range = "9999"

        with allure.step("Given the user is on the search screen"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"When searching for hymn number '{number_out_of_range}'"):
            search_page.search_hymn(number_out_of_range)

        with allure.step("Then a Toast is displayed indicating the valid number range"):
            toast_text = search_page.get_toast_message()
            assert toast_text.startswith("El número debe estar entre 1 al "), (
                f"Expected Toast starting with 'El número debe estar entre 1 al ', but got '{toast_text}'"
            )

    @allure.title("SCN-BUS-004: Validate warning Toast on invalid alphanumeric input")
    def test_search_hymn_by_mixed_input_shows_validation_toast(self, driver):
        mixed_query = "12abc"

        with allure.step("Given the user is on the search screen"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"When searching with mixed alphanumeric input '{mixed_query}'"):
            search_page.search_hymn(mixed_query)

        with allure.step("Then a Toast alerts against mixing text and numbers"):
            toast_text = search_page.get_toast_message()
            assert toast_text == "No se permite mezclar texto y números", (
                f"Expected Toast 'No se permite mezclar texto y números', but got '{toast_text}'"
            )

    @allure.title("SCN-BUS-005: Validate warning Toast on invalid special characters")
    def test_search_hymn_by_invalid_characters_shows_general_validation_toast(self, driver):
        invalid_query = "@@@"

        with allure.step("Given the user is on the search screen"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"When searching with invalid special characters '{invalid_query}'"):
            search_page.search_hymn(invalid_query)

        with allure.step("Then a Toast is displayed showing the allowed format rule"):
            toast_text = search_page.get_toast_message()
            assert toast_text.startswith("Solo se permite texto o números entre 1 al "), (
                f"Expected Toast starting with 'Solo se permite texto o números entre 1 al ', but got '{toast_text}'"
            )

    @allure.title("SCN-BUS-006: Search hymn by number and open result")
    def test_search_hymn_by_number_and_open_result(self, driver):
        hymn_query = "1"

        with allure.step("Given the user is on the search screen"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"When searching for hymn '{hymn_query}'"):
            search_page.search_hymn(hymn_query)

        with allure.step("And matching results are returned"):
            assert search_page.get_results_count() > 0, f"No results found when searching for '{hymn_query}'"

        with allure.step(f"When opening hymn #{hymn_query} from the results list"):
            hymn_page = search_page.open_hymn_by_number(1)

        with allure.step("Then the hymn detail view is displayed with a non-empty title"):
            actual_title = hymn_page.get_title()
            assert actual_title != "", "Hymn title in detail view is unexpectedly empty"
