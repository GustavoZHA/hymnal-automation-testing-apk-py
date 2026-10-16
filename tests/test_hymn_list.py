import allure
import pytest

from pages.home_page import HomePage


@allure.epic("Himnario Móvil")
@allure.feature("Lista de Himnos")
class TestHymnList:

    @allure.title("SCN-LIS-001: Abrir lista de himnos y seleccionar un himno por su título")
    def test_open_hymn_list_and_open_by_title(self, driver):
        target_title = "Ven , ¡oh Todopoderoso!"

        with allure.step("Dado que el usuario abre la lista de himnos desde el Home"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()

        with allure.step(f"Cuando selecciona el himno por su título '{target_title}'"):
            hymn_page = hymn_list.open_hymn_by_title(target_title)

        with allure.step("Entonces el detalle del himno se carga con un título no vacío"):
            actual_title = hymn_page.get_title()
            assert actual_title != "", "El título del himno está vacío"
            assert target_title in actual_title, f"Se esperaba '{target_title}' en '{actual_title}'"

    @allure.title("SCN-LIS-002: Abrir lista de himnos y seleccionar el himno #1 por su número")
    def test_open_hymn_list_and_open_by_number(self, driver):
        hymn_number = 1
        expected_title = "1. Ven , ¡oh Todopoderoso!"

        with allure.step("Dado que el usuario abre la lista de himnos desde el Home"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()

        with allure.step(f"Cuando selecciona el himno número {hymn_number}"):
            hymn_page = hymn_list.open_hymn_by_number(hymn_number)

        with allure.step(f"Entonces el título del himno en detalle coincide con '{expected_title}'"):
            actual_title = hymn_page.get_title()
            assert actual_title == expected_title, f"Se esperaba '{expected_title}' pero se obtuvo '{actual_title}'"
