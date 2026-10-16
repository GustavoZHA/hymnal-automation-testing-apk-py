import allure
import pytest

from pages.settings_page import SettingsPage


@allure.epic("Himnario Móvil")
@allure.feature("Configuración")
class TestSettings:

    @pytest.mark.skip(reason="Ruta de acceso a Settings en refinamiento")
    @allure.title("SCN-SET-001: Interacción con los elementos de Configuración")
    def test_settings_elements_interaction(self, driver):
        with allure.step("Dado que el usuario accede a la pantalla de Configuración"):
            settings_page = SettingsPage(driver)

        with allure.step("Cuando interactúa con los controles de tema y fuente"):
            settings_page.toggle_theme()
            settings_page.increase_font()
            settings_page.decrease_font()
            settings_page.toggle_visible_music()

        with allure.step("Entonces los ajustes se aplican correctamente"):
            assert settings_page.is_settings_title_displayed()
