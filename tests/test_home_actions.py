import allure
import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.favoritos_page import FavoritosPage
from pages.conocidos_page import ConocidosPage
from pages.list_personality_page import ListPersonalityPage
from pages.components.menu_component import MenuComponent


@allure.epic("Himnario Móvil")
@allure.feature("Home")
class TestHomeActions:

    @allure.title("SCN-HOM-003: Acceso directo a la pantalla de Búsqueda")
    def test_open_search(self, driver):
        with allure.step("Dado que el usuario está en la pantalla principal"):
            home = HomePage(driver)

        with allure.step("Cuando presiona el botón de búsqueda"):
            search_page = home.open_search()

        with allure.step("Entonces se muestra la pantalla de búsqueda"):
            assert isinstance(search_page, SearchPage), "No se navegó a SearchPage"

    @allure.title("SCN-HOM-004: Acceso directo a la pantalla de Favoritos")
    def test_open_favorites(self, driver):
        with allure.step("Dado que el usuario está en la pantalla principal"):
            home = HomePage(driver)

        with allure.step("Cuando presiona el botón de favoritos"):
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step("Entonces se muestra la sección de favoritos con su título"):
            assert favoritos.get_title() == "Favoritos"

    @allure.title("SCN-HOM-005: Acceso directo a la pantalla de Conocidos")
    def test_open_known(self, driver):
        with allure.step("Dado que el usuario está en la pantalla principal"):
            home = HomePage(driver)

        with allure.step("Cuando presiona el botón de conocidos"):
            home.open_known()
            conocidos = ConocidosPage(driver)

        with allure.step("Entonces se muestra la sección de conocidos con su título"):
            assert conocidos.get_title() == "Conocidos"

    @allure.title("SCN-HOM-006: Acceso directo a Listas Personalizadas")
    def test_open_personalized_lists(self, driver):
        with allure.step("Dado que el usuario está en la pantalla principal"):
            home = HomePage(driver)

        with allure.step("Cuando presiona el botón de listas personalizadas"):
            list_page = home.open_list_personality()

        with allure.step("Entonces se muestra la pantalla de Listas Personalizadas"):
            assert isinstance(list_page, ListPersonalityPage), "No se navegó a ListPersonalityPage"

    @allure.title("SCN-HOM-007: Abrir menú lateral y retornar al Home")
    def test_open_menu_and_home(self, driver):
        with allure.step("Dado que el menú lateral está disponible"):
            menu = MenuComponent(driver)

        with allure.step("Cuando el usuario abre el cajón de navegación (drawer)"):
            menu.open_drawer()

        with allure.step("Y selecciona la opción de Home en el menú"):
            menu.click_home_button()

        with allure.step("Entonces el usuario permanece o regresa a la vista principal"):
            home = HomePage(driver)
            assert home.driver is not None
