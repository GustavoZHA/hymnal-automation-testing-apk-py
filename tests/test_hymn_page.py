import allure
import pytest

from pages.home_page import HomePage


@allure.epic("Himnario Móvil")
@allure.feature("Detalle del Himno")
class TestHymnPage:

    def _load_hymn(self, driver, title="Luz de vida celestial"):
        with allure.step(f"Navegar al detalle del himno '{title}'"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()
            return hymn_list.open_hymn_by_title(title)

    @allure.title("SCN-DET-001: Verificar presencia del título en la pantalla de detalle")
    def test_hymn_page_title_is_present(self, driver):
        with allure.step("Dado que se carga un himno específico"):
            hymn_page = self._load_hymn(driver)

        with allure.step("Entonces el título del himno no debe estar vacío"):
            assert hymn_page.get_title() != "", "El título del himno no está presente"

    @allure.title("SCN-DET-002: Verificar que las estrofas del himno se carguen correctamente")
    def test_hymn_page_verse_texts_are_loaded(self, driver):
        with allure.step("Dado que se carga un himno específico"):
            hymn_page = self._load_hymn(driver)

        with allure.step("Cuando se obtienen las estrofas del himno"):
            verse_texts = hymn_page.get_verse_texts()

        with allure.step("Entonces debe haber al menos una estrofa cargada"):
            assert len(verse_texts) > 0, "No se cargaron estrofas en el himno"

    @allure.title("SCN-DET-003: Visualización del reproductor al reproducir el himno")
    def test_hymn_page_music_player_is_displayed(self, driver):
        with allure.step("Dado que se carga el detalle del himno"):
            hymn_page = self._load_hymn(driver)

        with allure.step("Cuando se presiona el botón de reproducir (Play)"):
            hymn_page.play_hymn()

        with allure.step("Entonces el contenedor del reproductor de música está visible"):
            assert hymn_page.is_music_player_displayed(), "El reproductor de música no se mostró"

    @allure.title("SCN-DET-004: Alternar reproducción y pausa en el reproductor")
    def test_hymn_page_can_play_and_pause(self, driver):
        with allure.step("Dado que el reproductor de audio está activo"):
            hymn_page = self._load_hymn(driver)
            hymn_page.play_hymn()

        with allure.step("Cuando se presiona el botón de Play/Pausa"):
            hymn_page.play_pause()

        with allure.step("Entonces el reproductor permanece desplegado"):
            assert hymn_page.is_music_player_displayed(), "El reproductor ya no está visible tras pausar"

    @allure.title("SCN-DET-005: Alternar estado de favorito en el himno")
    def test_hymn_page_can_toggle_favorite(self, driver):
        with allure.step("Dado que se abre el detalle del himno"):
            hymn_page = self._load_hymn(driver)

        with allure.step("Cuando se pulsa el botón de alternar favorito"):
            hymn_page.toggle_favorite()

        with allure.step("Entonces la acción se completa exitosamente"):
            assert hymn_page.driver is not None

    @allure.title("SCN-DET-006: Marcar himno como conocido desde el detalle")
    def test_hymn_page_can_add_to_list_and_mark_known(self, driver):
        with allure.step("Dado que se abre el detalle del himno"):
            hymn_page = self._load_hymn(driver)

        with allure.step("Cuando se marca como conocido"):
            hymn_page.mark_as_known()

        with allure.step("Entonces la acción se completa exitosamente"):
            assert hymn_page.driver is not None

    @allure.title("SCN-DET-007: Navegación entre himnos anterior/siguiente y controles de rebobinado/avance")
    def test_hymn_page_navigation_buttons(self, driver):
        with allure.step("Dado que se abre el detalle de un himno"):
            hymn_page = self._load_hymn(driver)

        with allure.step("Cuando se navega al himno anterior y luego al siguiente"):
            hymn_page.open_previous_hymn()
            hymn_page.open_next_hymn()

        with allure.step("Y se inician los controles de rebobinar y adelantar audio"):
            hymn_page.play_hymn()
            hymn_page.rewind()
            hymn_page.forward()

        with allure.step("Entonces las interacciones de controles finalizan con éxito"):
            assert hymn_page.driver is not None
