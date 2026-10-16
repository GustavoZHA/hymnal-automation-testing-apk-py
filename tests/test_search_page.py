import allure
import pytest

from pages.home_page import HomePage
from locators.search_locators import SearchLocators


@allure.epic("Himnario Móvil")
@allure.feature("Búsqueda de Himnos")
class TestSearchPage:

    @allure.title("SCN-BUS-001: Verificar presencia de elementos en la pantalla de búsqueda")
    def test_open_search_page_and_verify_elements(self, driver):
        with allure.step("Dado que el usuario navega a la pantalla de búsqueda"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step("Entonces el campo de entrada y el botón de búsqueda están visibles"):
            assert search_page.is_displayed(SearchLocators.SEARCH_INPUT), "Campo de búsqueda no visible"
            assert search_page.is_displayed(SearchLocators.SEARCH_BUTTON), "Botón de búsqueda no visible"

    @allure.title("SCN-BUS-002: Validar mensaje al ingresar texto menor a 5 caracteres")
    def test_search_hymn_by_short_text_shows_validation_toast(self, driver):
        search_query = "des"

        with allure.step("Dado que el usuario está en la pantalla de búsqueda"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"Cuando busca con un texto corto '{search_query}'"):
            search_page.search_hymn(search_query)

        with allure.step("Entonces se muestra el mensaje Toast de validación de longitud mínima"):
            toast_text = search_page.get_toast_message()
            assert toast_text == "El texto debe tener más de 5 caracteres"

    @allure.title("SCN-BUS-003: Validar mensaje al ingresar número fuera de rango")
    def test_search_hymn_by_number_out_of_range_shows_validation_toast(self, driver):
        number_out_of_range = "9999"

        with allure.step("Dado que el usuario está en la pantalla de búsqueda"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"Cuando busca el número '{number_out_of_range}'"):
            search_page.search_hymn(number_out_of_range)

        with allure.step("Entonces se muestra un Toast indicando el rango válido permitido"):
            toast_text = search_page.get_toast_message()
            assert toast_text.startswith("El número debe estar entre 1 al ")

    @allure.title("SCN-BUS-004: Validar mensaje al ingresar combinación alfanumérica no permitida")
    def test_search_hymn_by_mixed_input_shows_validation_toast(self, driver):
        mixed_query = "12abc"

        with allure.step("Dado que el usuario está en la pantalla de búsqueda"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"Cuando ingresa una búsqueda mixta '{mixed_query}'"):
            search_page.search_hymn(mixed_query)

        with allure.step("Entonces se muestra un Toast alertando sobre no mezclar texto y números"):
            toast_text = search_page.get_toast_message()
            assert toast_text == "No se permite mezclar texto y números"

    @allure.title("SCN-BUS-005: Validar mensaje al ingresar caracteres especiales inválidos")
    def test_search_hymn_by_invalid_characters_shows_general_validation_toast(self, driver):
        invalid_query = "@@@"

        with allure.step("Dado que el usuario está en la pantalla de búsqueda"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"Cuando busca con caracteres inválidos '{invalid_query}'"):
            search_page.search_hymn(invalid_query)

        with allure.step("Entonces se muestra el Toast con la regla de formato permitida"):
            toast_text = search_page.get_toast_message()
            assert toast_text.startswith("Solo se permite texto o números entre 1 al ")

    @allure.title("SCN-BUS-006: Buscar himno por número y abrir resultado")
    def test_search_hymn_by_number_and_open_result(self, driver):
        hymn_query = "1"

        with allure.step("Dado que el usuario está en la pantalla de búsqueda"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"Cuando busca el himno '{hymn_query}'"):
            search_page.search_hymn(hymn_query)

        with allure.step("Y se obtienen resultados coincidentes"):
            assert search_page.get_results_count() > 0, "No se obtuvieron resultados para la búsqueda"

        with allure.step(f"Cuando abre el himno #{hymn_query} de la lista de resultados"):
            hymn_page = search_page.open_hymn_by_number(1)

        with allure.step("Entonces se visualiza la pantalla del himno con título válido"):
            assert hymn_page.get_title() != "", "El título del himno obtenido está vacío"
