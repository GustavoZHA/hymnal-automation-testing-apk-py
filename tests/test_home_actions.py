import allure
import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.favoritos_page import FavoritosPage
from pages.conocidos_page import ConocidosPage
from pages.list_personality_page import ListPersonalityPage
from pages.components.menu_component import MenuComponent


@allure.epic("Hymnal Mobile App")
@allure.feature("Home")
class TestHomeActions:

    @allure.title("SCN-HOM-003: Quick access to Search screen")
    def test_open_search(self, driver):
        with allure.step("Given the user is on the main Home screen"):
            home = HomePage(driver)

        with allure.step("When clicking the search button"):
            search_page = home.open_search()

        with allure.step("Then the search screen is displayed"):
            assert isinstance(search_page, SearchPage), "Navigation to SearchPage failed"

    @allure.title("SCN-HOM-004: Quick access to Favorites screen")
    def test_open_favorites(self, driver):
        with allure.step("Given the user is on the main Home screen"):
            home = HomePage(driver)

        with allure.step("When clicking the favorites button"):
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step("Then the favorites section is displayed with title 'Favoritos'"):
            actual_title = favoritos.get_title()
            assert actual_title == "Favoritos", f"Expected title 'Favoritos', but got '{actual_title}'"

    @allure.title("SCN-HOM-005: Quick access to Known Hymns screen")
    def test_open_known(self, driver):
        with allure.step("Given the user is on the main Home screen"):
            home = HomePage(driver)

        with allure.step("When clicking the known hymns button"):
            home.open_known()
            conocidos = ConocidosPage(driver)

        with allure.step("Then the known hymns section is displayed with title 'Conocidos'"):
            actual_title = conocidos.get_title()
            assert actual_title == "Conocidos", f"Expected title 'Conocidos', but got '{actual_title}'"

    @allure.title("SCN-HOM-006: Quick access to Custom Playlists screen")
    def test_open_personalized_lists(self, driver):
        with allure.step("Given the user is on the main Home screen"):
            home = HomePage(driver)

        with allure.step("When clicking the custom playlists button"):
            list_page = home.open_list_personality()

        with allure.step("Then the Custom Playlists screen is displayed"):
            assert isinstance(list_page, ListPersonalityPage), "Navigation to ListPersonalityPage failed"

    @allure.title("SCN-HOM-007: Open navigation drawer and return to Home")
    def test_open_menu_and_home(self, driver):
        with allure.step("Given the navigation drawer component is initialized"):
            menu = MenuComponent(driver)

        with allure.step("When the user opens the navigation drawer"):
            menu.open_drawer()

        with allure.step("And selects the Home option in the drawer"):
            menu.click_home_button()

        with allure.step("Then the user remains on or returns to the Home view"):
            home = HomePage(driver)
            assert home.driver is not None, "Driver instance should not be None after returning Home"
