import allure
import pytest

from pages.home_page import HomePage
from pages.conocidos_page import ConocidosPage
from pages.hymn_page import HymnPage


@allure.epic("Himnario Móvil")
@allure.feature("Himnos Conocidos")
class TestConocidos:

    @allure.title("SCN-CON-001: Abrir pantalla de Conocidos desde Home y verificar título")
    def test_open_conocidos(self, driver):
        with allure.step("Dado que el usuario se encuentra en la pantalla principal"):
            home = HomePage(driver)

        with allure.step("Cuando navega a la sección de 'Conocidos'"):
            home.open_known()
            conocidos = ConocidosPage(driver)

        with allure.step("Entonces el título de la página debe ser 'Conocidos'"):
            actual_title = conocidos.get_title()
            assert actual_title == "Conocidos", f"Se esperaba 'Conocidos' pero se obtuvo '{actual_title}'"

    @allure.title("SCN-CON-002: Marcar himno como conocido y verificar su acceso en la lista de Conocidos")
    def test_open_and_add_hymn_in_conocidos(self, driver):
        hymn_number = 12
        hymn_title = "Cúan firme cimiento"

        with allure.step(f"Dado que el usuario ingresa al himnario y marca el himno #{hymn_number} como conocido"):
            home = HomePage(driver)
            hymn_list_page = home.open_hymnal()
            hymn_page = hymn_list_page.open_hymn_by_number(hymn_number)
            hymn_page.mark_as_known()

        with allure.step("Y regresa al Home e ingresa a la sección 'Conocidos'"):
            hymn_list_page.click_home_button()
            home.open_known()
            conocidos = ConocidosPage(driver)

        with allure.step(f"Cuando abre el himno #{hymn_number} desde la lista de Conocidos"):
            opened_hymn_page = conocidos.open_hymn_by_number(hymn_number)

        with allure.step(f"Entonces el detalle del himno muestra el número '{hymn_number}' y el título '{hymn_title}'"):
            page_title = opened_hymn_page.get_title()
            assert f"{hymn_number}" in page_title, f"El número '{hymn_number}' no está en '{page_title}'"
            assert hymn_title in page_title, f"El título '{hymn_title}' no está en '{page_title}'"
            assert isinstance(opened_hymn_page, HymnPage)

    @allure.title("SCN-CON-003: Regresar al Home desde la pantalla de Conocidos")
    def test_navigate_from_conocidos_to_home(self, driver):
        with allure.step("Dado que el usuario navega a la sección de 'Conocidos'"):
            home = HomePage(driver)
            home.open_known()
            conocidos = ConocidosPage(driver)

        with allure.step("Cuando presiona el botón para ir a Home"):
            home_page = conocidos.go_to_home()

        with allure.step("Entonces el usuario se encuentra de regreso en la página principal"):
            assert isinstance(home_page, HomePage)
