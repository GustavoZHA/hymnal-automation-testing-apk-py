import allure
import pytest

from pages.home_page import HomePage
from pages.hymn_list_page import HymnListPage
from pages.hymn_page import HymnPage


@allure.epic("Himnario Móvil")
@allure.feature("Home")
class TestHome:

    @allure.title("SCN-HOM-001: Abrir lista de himnos desde el botón principal del Home")
    def test_open_hymnal(self, driver):
        with allure.step("Dado que el usuario se encuentra en la pantalla principal"):
            home = HomePage(driver)

        with allure.step("Cuando presiona el botón 'Himnario'"):
            hymn_list = home.open_hymnal()

        with allure.step("Entonces se muestra la pantalla de la lista de himnos"):
            assert isinstance(hymn_list, HymnListPage), "No se navegó a HymnListPage"

    @allure.title("SCN-HOM-002: Navegar desde Home a la lista y abrir un himno por título")
    def test_open_hymn_by_title(self, driver):
        target_title = "Ven , ¡oh Todopoderoso!"

        with allure.step("Dado que el usuario abre la lista general de himnos desde el Home"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()

        with allure.step(f"Cuando selecciona el himno '{target_title}'"):
            hymn_page = hymn_list.open_hymn_by_title(target_title)

        with allure.step(f"Entonces se abre la vista de detalle del himno con el título '{target_title}'"):
            actual_title = hymn_page.get_title()
            assert target_title in actual_title, f"Se esperaba '{target_title}' en el título, obtenido: '{actual_title}'"
            assert isinstance(hymn_page, HymnPage)
