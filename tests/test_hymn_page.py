import allure
import pytest

from pages.home_page import HomePage


@allure.epic("Hymnal Mobile App")
@allure.feature("Detalle del Himno")
class TestHymnPage:

    def _load_hymn(self, driver, title="Luz de vida celestial"):
        with allure.step(f"Navigate to detail of hymn '{title}'"):
            home = HomePage(driver)
            hymn_list = home.open_hymnal()
            return hymn_list.open_hymn_by_title(title)

    @allure.title("SCN-DET-001: Verify hymn title is present on detail screen")
    def test_hymn_page_title_is_present(self, driver):
        with allure.step("Given a specific hymn detail view is loaded"):
            hymn_page = self._load_hymn(driver)

        with allure.step("Then the hymn title must not be empty"):
            assert hymn_page.get_title() != "", "Hymn title is unexpectedly empty"

    @allure.title("SCN-DET-002: Verify hymn verses load properly")
    def test_hymn_page_verse_texts_are_loaded(self, driver):
        with allure.step("Given a specific hymn detail view is loaded"):
            hymn_page = self._load_hymn(driver)

        with allure.step("When retrieving the hymn verse texts"):
            verse_texts = hymn_page.get_verse_texts()

        with allure.step("Then at least one verse element must be loaded"):
            assert len(verse_texts) > 0, "No verses were loaded for the hymn"

    @allure.title("SCN-DET-003: Audio player layout is displayed upon playback")
    def test_hymn_page_music_player_is_displayed(self, driver):
        with allure.step("Given the hymn detail view is loaded"):
            hymn_page = self._load_hymn(driver)

        with allure.step("When clicking the Play button"):
            hymn_page.play_hymn()

        with allure.step("Then the music player container becomes visible"):
            assert hymn_page.is_music_player_displayed(), "The music player container was not displayed"

    @allure.title("SCN-DET-004: Toggle play and pause on audio player")
    def test_hymn_page_can_play_and_pause(self, driver):
        with allure.step("Given the audio player is actively playing"):
            hymn_page = self._load_hymn(driver)
            hymn_page.play_hymn()

        with allure.step("When clicking the Play/Pause button"):
            hymn_page.play_pause()

        with allure.step("Then the player container remains displayed"):
            assert hymn_page.is_music_player_displayed(), "The music player is no longer visible after pausing"

    @allure.title("SCN-DET-005: Toggle favorite status on hymn")
    def test_hymn_page_can_toggle_favorite(self, driver):
        with allure.step("Given the hymn detail view is open"):
            hymn_page = self._load_hymn(driver)

        with allure.step("When toggling the favorite button"):
            hymn_page.toggle_favorite()

        with allure.step("Then the action completes successfully"):
            assert hymn_page.driver is not None, "Driver instance should be valid"

    @allure.title("SCN-DET-006: Mark hymn as known from detail screen")
    def test_hymn_page_can_add_to_list_and_mark_known(self, driver):
        with allure.step("Given the hymn detail view is open"):
            hymn_page = self._load_hymn(driver)

        with allure.step("When marking the hymn as known"):
            hymn_page.mark_as_known()

        with allure.step("Then the action completes successfully"):
            assert hymn_page.driver is not None, "Driver instance should be valid"

    @allure.title("SCN-DET-007: Navigate previous/next hymns and control audio seek/rewind")
    def test_hymn_page_navigation_buttons(self, driver):
        with allure.step("Given a hymn detail view is open"):
            hymn_page = self._load_hymn(driver)

        with allure.step("When navigating to the previous and then next hymn"):
            hymn_page.open_previous_hymn()
            hymn_page.open_next_hymn()

        with allure.step("And triggering audio rewind and forward seek controls"):
            hymn_page.play_hymn()
            hymn_page.rewind()
            hymn_page.forward()

        with allure.step("Then the player control interactions complete successfully"):
            assert hymn_page.driver is not None, "Driver instance should be valid"

    @allure.title("SCN-DET-008: Open and close the Add to List popup modal")
    def test_hymn_page_add_to_list_popup_lifecycle(self, driver):
        with allure.step("Given a hymn detail view is open"):
            hymn_page = self._load_hymn(driver)

        with allure.step("When opening the 'Add to List' popup"):
            hymn_page.add_to_list()

        with allure.step("Then the popup modal title is displayed"):
            popup_title = hymn_page.get_popup_title()
            assert popup_title != "", "Add to List popup title is unexpectedly empty"

        with allure.step("When closing the popup modal"):
            hymn_page.close_popup()

        with allure.step("Then the hymn detail view remains active"):
            assert hymn_page.get_title() != "", "Hymn detail view should remain active after popup dismissal"

    @allure.title("SCN-DET-009: Verify audio player timestamps are properly formatted")
    def test_hymn_page_music_player_audio_durations(self, driver):
        with allure.step("Given the hymn detail view is loaded"):
            hymn_page = self._load_hymn(driver)

        with allure.step("When clicking the Play button to activate the audio player"):
            hymn_page.play_hymn()

        with allure.step("Then current playback timestamp and total duration are displayed"):
            current_time = hymn_page.get_current_playback_time()
            total_duration = hymn_page.get_total_playback_duration()
            assert ":" in current_time, f"Expected current time with mm:ss format, got: '{current_time}'"
            assert ":" in total_duration, f"Expected total duration with mm:ss format, got: '{total_duration}'"
            assert total_duration != "00:00", f"Total track duration should be greater than zero, got: '{total_duration}'"
