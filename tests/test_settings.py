import allure
import pytest

from pages.settings_page import SettingsPage


@allure.epic("Hymnal Mobile App")
@allure.feature("Configuración")
class TestSettings:

    @pytest.mark.skip(reason="Navigation path to Settings is currently under refinement")
    @allure.title("SCN-SET-001: Interaction with Settings configuration toggles")
    def test_settings_elements_interaction(self, driver):
        with allure.step("Given the user accesses the Settings screen"):
            settings_page = SettingsPage(driver)

        with allure.step("When interacting with theme, font size, and music visibility controls"):
            settings_page.toggle_theme()
            settings_page.increase_font()
            settings_page.decrease_font()
            settings_page.toggle_visible_music()

        with allure.step("Then the settings are applied and the screen title remains visible"):
            assert settings_page.is_settings_title_displayed(), "Settings screen title is not displayed"
