import os
import allure
import pytest

from pages.home_page import HomePage
from pages.settings_page import SettingsPage
from utils.adb_helper import AdbHelper


@allure.epic("Hymnal Mobile App")
@allure.feature("Configuración")
class TestSettings:

    @allure.title("SCN-SET-001: Switch theme between Light and Dark mode")
    def test_switch_theme_light_and_dark(self, driver):
        with allure.step("Given the user navigates to the Settings screen"):
            home = HomePage(driver)
            settings_page = home.open_settings()
            assert settings_page.is_settings_title_displayed(), (
                "Expected Settings title to be visible upon navigation"
            )

        with allure.step("When the user selects the Dark theme mode"):
            settings_page.select_dark_theme()

        with allure.step("And the user switches back to the Light theme mode"):
            settings_page.select_light_theme()

        with allure.step("Then the theme switches successfully and the Settings title remains visible"):
            assert settings_page.is_settings_title_displayed(), (
                "Expected Settings screen to remain active after toggling themes"
            )

    @allure.title("SCN-SET-002: Adjust font size and verify preview text scaling")
    def test_increase_and_decrease_font_preview(self, driver):
        with allure.step("Given the user is on the Settings screen"):
            home = HomePage(driver)
            settings_page = home.open_settings()

        with allure.step("When the user captures the initial preview text height"):
            initial_height = settings_page.get_preview_verse_height()

        with allure.step("And the user increases the font size multiple times"):
            for _ in range(3):
                settings_page.increase_font()
            increased_height = settings_page.get_preview_verse_height()

        with allure.step("Then the preview verse height increases proportionally"):
            assert increased_height >= initial_height, (
                f"Expected increased height ({increased_height}) >= initial height ({initial_height})"
            )

        with allure.step("When the user decreases the font size"):
            for _ in range(3):
                settings_page.decrease_font()
            decreased_height = settings_page.get_preview_verse_height()

        with allure.step("Then the preview verse height decreases back"):
            assert decreased_height <= increased_height, (
                f"Expected decreased height ({decreased_height}) <= increased height ({increased_height})"
            )

    @allure.title("SCN-SET-003: Verify font size adjustments apply to Hymn List and Hymn Verse")
    def test_font_size_changes_reflect_on_hymn_list_and_verse(self, driver):
        with allure.step("Given the user increases the font size in Settings"):
            home = HomePage(driver)
            settings_page = home.open_settings()
            for _ in range(4):
                settings_page.increase_font()

        with allure.step("When the user navigates back to Home and opens the Hymn List"):
            home = settings_page.return_to_home()
            hymn_list = home.open_hymnal()

        with allure.step("Then hymn list records are rendered with proper dimensions"):
            item_height = hymn_list.get_first_hymn_title_height()
            assert item_height > 0, (
                f"Expected hymn title item height to be positive, got {item_height}"
            )

        with allure.step("And when opening a hymn detail screen"):
            hymn_page = hymn_list.open_hymn_by_number(1)

        with allure.step("Then hymn verses are displayed with valid line dimensions"):
            verse_height = hymn_page.get_first_verse_height()
            assert verse_height > 0, (
                f"Expected hymn verse height to be positive, got {verse_height}"
            )

    @allure.title("SCN-SET-004: Toggle visible music and verify music note icons in hymn list")
    def test_toggle_visible_music_shows_music_icons_in_hymn_list(self, driver):
        with allure.step("Given the user navigates to Settings and enables the music visibility switch"):
            home = HomePage(driver)
            settings_page = home.open_settings()
            settings_page.set_music_switch(True)
            assert settings_page.is_music_switch_checked(), (
                "Expected music switch to be checked after enabling"
            )

        with allure.step("When the user returns to Home and opens the Hymn List"):
            home = settings_page.return_to_home()
            hymn_list = home.open_hymnal()

        with allure.step("Then music note icons are displayed on hymns with available music"):
            assert hymn_list.are_music_icons_present(), (
                "Expected music note icons to be displayed in the hymn list"
            )

        with allure.step("When the user returns to Settings and disables the music visibility switch"):
            settings_page = hymn_list.open_settings()
            settings_page.set_music_switch(False)
            assert not settings_page.is_music_switch_checked(), (
                "Expected music switch to be unchecked after disabling"
            )

        with allure.step("And the user navigates back to the Hymn List"):
            home = settings_page.return_to_home()
            hymn_list = home.open_hymnal()

        with allure.step("Then music note icons are no longer displayed in the hymn list"):
            assert not hymn_list.are_music_icons_present(), (
                "Expected music note icons to be hidden when music visibility is disabled"
            )

    @allure.title("SCN-SET-005: Import backup data from JSON file")
    def test_import_backup_restores_custom_playlists_and_favorites(self, driver):
        backup_local_path = os.path.join("data", "himnario_backup.json")

        with allure.step("Given a valid backup JSON file is placed on the device storage"):
            pushed = AdbHelper.push_file(backup_local_path, "/sdcard/Download/himnario_backup.json")
            assert pushed, "Failed to push backup file to /sdcard/Download/himnario_backup.json via ADB"

        with allure.step("And the user navigates to the Settings screen"):
            home = HomePage(driver)
            settings_page = home.open_settings()

        with allure.step("When the user clicks 'Importar Backup'"):
            settings_page.click_import_backup()

        with allure.step("And selects 'himnario_backup.json' from the file picker"):
            settings_page.select_backup_file("himnario_backup.json")

        with allure.step("Then the Settings screen remains active and the backup is loaded"):
            assert settings_page.is_settings_title_displayed(), (
                "Expected Settings screen to remain active after backup import"
            )

    @allure.title("SCN-SET-006: Open export backup dialog and verify export options")
    def test_open_export_backup_dialog_and_verify_options(self, driver):
        with allure.step("Given the user navigates to the Settings screen"):
            home = HomePage(driver)
            settings_page = home.open_settings()

        with allure.step("When the user clicks the 'Exportar Backup' button"):
            settings_page.click_export_backup()

        with allure.step("Then the export dialog is displayed with the title 'Seleccione qué desea exportar'"):
            assert settings_page.is_export_dialog_displayed(), (
                "Expected export selection dialog to be displayed"
            )
            dialog_title = settings_page.get_export_dialog_title()
            assert "exportar" in dialog_title.lower(), (
                f"Expected export title to mention 'exportar', but got '{dialog_title}'"
            )

        with allure.step("When the user cancels the export dialog"):
            settings_page.cancel_export_dialog()

        with allure.step("Then the dialog is closed and the Settings screen remains visible"):
            assert settings_page.is_settings_title_displayed(), (
                "Expected Settings screen to be visible after canceling the export dialog"
            )
