import allure
import pytest

from pages.home_page import HomePage
from pages.favoritos_page import FavoritosPage
from pages.hymn_page import HymnPage


@allure.epic("Hymnal Mobile App")
@allure.feature("Favoritos")
class TestFavoritos:

    @allure.title("SCN-FAV-001: Open Favorites screen from Home and verify title")
    def test_open_favoritos(self, driver):
        with allure.step("Given the user is on the main Home screen"):
            home = HomePage(driver)

        with allure.step("When navigating to the 'Favoritos' section"):
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step("Then the screen title must be 'Favoritos'"):
            actual_title = favoritos.get_title()
            assert actual_title == "Favoritos", f"Expected title 'Favoritos', but got '{actual_title}'"

    @allure.title("SCN-FAV-002: Add hymn to favorites and verify opening from Favorites list")
    def test_open_hymn_by_title_from_favoritos(self, driver):
        hymn_title = "Alma mía no delires"

        with allure.step(f"Given the user locates hymn '{hymn_title}' and marks it as favorite"):
            home = HomePage(driver)
            hymn_list_page = home.open_hymnal()
            hymn_page = hymn_list_page.open_hymn_by_title(hymn_title)
            hymn_page.toggle_favorite()

        with allure.step("And navigates back Home to open the 'Favoritos' section"):
            hymn_list_page.click_home_button()
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step(f"When opening hymn '{hymn_title}' from the Favorites list"):
            opened_hymn_page = favoritos.open_hymn_by_title(hymn_title)

        with allure.step(f"Then the hymn detail view displays title containing '{hymn_title}'"):
            actual_title = opened_hymn_page.get_title()
            assert hymn_title in actual_title, f"Expected hymn title '{hymn_title}' in '{actual_title}'"
            assert isinstance(opened_hymn_page, HymnPage), "Expected instance of HymnPage"

    @allure.title("SCN-FAV-003: Return to Home from Favorites screen")
    def test_navigate_from_favoritos_to_home(self, driver):
        with allure.step("Given the user navigates to the 'Favoritos' section"):
            home = HomePage(driver)
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step("When clicking the button to return Home"):
            home_page = favoritos.go_to_home()

        with allure.step("Then the user is back on the main Home screen"):
            assert isinstance(home_page, HomePage), "Expected instance of HomePage"

    @allure.title("SCN-FAV-004: Open hymn by number from Favorites screen")
    def test_open_hymn_by_number_from_favoritos(self, driver):
        hymn_number = 1

        with allure.step(f"Given hymn #{hymn_number} is added to favorites"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()
            hymn_page = hymn_list.open_hymn_by_number(hymn_number)
            hymn_page.toggle_favorite()

        with allure.step("And the user navigates to the 'Favoritos' section"):
            hymn_page.click_home_button()
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step(f"When opening hymn #{hymn_number} from the Favorites list"):
            opened_hymn_page = favoritos.open_hymn_by_number(hymn_number)

        with allure.step(f"Then the hymn detail view displays number '{hymn_number}'"):
            actual_title = opened_hymn_page.get_title()
            assert f"{hymn_number}" in actual_title, f"Expected hymn number '{hymn_number}' in '{actual_title}'"
            assert isinstance(opened_hymn_page, HymnPage), "Expected instance of HymnPage"
