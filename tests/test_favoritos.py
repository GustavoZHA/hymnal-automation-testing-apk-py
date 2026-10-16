import allure
import pytest

from pages.home_page import HomePage
from pages.favoritos_page import FavoritosPage
from pages.hymn_page import HymnPage


@allure.epic("Himnario Móvil")
@allure.feature("Favoritos")
class TestFavoritos:

    @allure.title("SCN-FAV-001: Abrir pantalla de Favoritos desde Home y verificar título")
    def test_open_favoritos(self, driver):
        with allure.step("Dado que el usuario se encuentra en la pantalla principal"):
            home = HomePage(driver)

        with allure.step("Cuando navega a la sección de 'Favoritos'"):
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step("Entonces el título de la pantalla debe ser 'Favoritos'"):
            actual_title = favoritos.get_title()
            assert actual_title == "Favoritos", f"Se esperaba 'Favoritos' pero se obtuvo '{actual_title}'"

    @allure.title("SCN-FAV-002: Agregar himno a favoritos y verificar su apertura desde la lista de Favoritos")
    def test_open_hymn_by_title_from_favoritos(self, driver):
        hymn_title = "Alma mía no delires"

        with allure.step(f"Dado que el usuario busca el himno '{hymn_title}' y lo marca como favorito"):
            home = HomePage(driver)
            hymn_list_page = home.open_hymnal()
            hymn_page = hymn_list_page.open_hymn_by_title(hymn_title)
            hymn_page.toggle_favorite()

        with allure.step("Y regresa al Home y accede a la sección de 'Favoritos'"):
            hymn_list_page.click_home_button()
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step(f"Cuando abre el himno '{hymn_title}' desde la lista de Favoritos"):
            opened_hymn_page = favoritos.open_hymn_by_title(hymn_title)

        with allure.step(f"Entonces el detalle del himno muestra el título '{hymn_title}'"):
            assert hymn_title in opened_hymn_page.get_title(), f"El título '{hymn_title}' no está en '{opened_hymn_page.get_title()}'"
            assert isinstance(opened_hymn_page, HymnPage)

    @allure.title("SCN-FAV-003: Regresar al Home desde la pantalla de Favoritos")
    def test_navigate_from_favoritos_to_home(self, driver):
        with allure.step("Dado que el usuario navega a la sección de 'Favoritos'"):
            home = HomePage(driver)
            home.open_favorites()
            favoritos = FavoritosPage(driver)

        with allure.step("Cuando presiona el botón para ir al Home"):
            home_page = favoritos.go_to_home()

        with allure.step("Entonces el usuario se encuentra en la pantalla principal"):
            assert isinstance(home_page, HomePage)
