import allure
import pytest

from pages.home_page import HomePage
from pages.conocidos_page import ConocidosPage
from pages.hymn_page import HymnPage


@allure.epic("Hymnal Mobile App")
@allure.feature("Himnos Conocidos")
class TestConocidos:

    @allure.title("SCN-CON-001: Open Known Hymns screen from Home and verify title")
    def test_open_conocidos(self, driver):
        with allure.step("Given the user is on the main Home screen"):
            home = HomePage(driver)

        with allure.step("When navigating to the 'Conocidos' section"):
            home.open_known()
            conocidos = ConocidosPage(driver)

        with allure.step("Then the screen title must be 'Conocidos'"):
            actual_title = conocidos.get_title()
            assert actual_title == "Conocidos", f"Expected title 'Conocidos', but got '{actual_title}'"

    @allure.title("SCN-CON-002: Mark hymn as known and verify access from Known list")
    def test_open_and_add_hymn_in_conocidos(self, driver):
        hymn_number = 12
        hymn_title = "Cúan firme cimiento"

        with allure.step(f"Given the user opens the hymnal and marks hymn #{hymn_number} as known"):
            home = HomePage(driver)
            hymn_list_page = home.open_hymnal()
            hymn_page = hymn_list_page.open_hymn_by_number(hymn_number)
            hymn_page.mark_as_known()

        with allure.step("And returns Home to access the 'Conocidos' section"):
            hymn_list_page.click_home_button()
            home.open_known()
            conocidos = ConocidosPage(driver)

        with allure.step(f"When opening hymn #{hymn_number} from the Known list"):
            opened_hymn_page = conocidos.open_hymn_by_number(hymn_number)

        with allure.step(f"Then the hymn detail view displays number '{hymn_number}' and title '{hymn_title}'"):
            page_title = opened_hymn_page.get_title()
            assert f"{hymn_number}" in page_title, f"Expected hymn number '{hymn_number}' in '{page_title}'"
            assert hymn_title in page_title, f"Expected hymn title '{hymn_title}' in '{page_title}'"
            assert isinstance(opened_hymn_page, HymnPage), "Expected instance of HymnPage"

    @allure.title("SCN-CON-003: Return to Home from Known Hymns screen")
    def test_navigate_from_conocidos_to_home(self, driver):
        with allure.step("Given the user navigates to the 'Conocidos' section"):
            home = HomePage(driver)
            home.open_known()
            conocidos = ConocidosPage(driver)

        with allure.step("When clicking the button to return Home"):
            home_page = conocidos.go_to_home()

        with allure.step("Then the user is back on the main Home screen"):
            assert isinstance(home_page, HomePage), "Expected instance of HomePage"
