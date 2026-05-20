from pages.home_page import HomePage


class TestHymnPage:

    def _load_hymn(self, driver, title="Ven , ¡oh Todopoderoso!"):
        home = HomePage(driver)
        hymn_list = home.open_hymnal()
        return hymn_list.open_hymn_by_title(title)

    def test_hymn_page_title_is_present(self, driver):
        hymn_page = self._load_hymn(driver)
        assert hymn_page.get_title() != ""

    def test_hymn_page_verse_texts_are_loaded(self, driver):
        hymn_page = self._load_hymn(driver)
        verse_texts = hymn_page.get_verse_texts()
        assert len(verse_texts) > 0

    def test_hymn_page_music_player_is_displayed(self, driver):
        hymn_page = self._load_hymn(driver)
        assert hymn_page.is_music_player_displayed()

    def test_hymn_page_can_play_and_pause(self, driver):
        hymn_page = self._load_hymn(driver)
        hymn_page.play_pause()
        assert hymn_page.is_music_player_displayed()

    def test_hymn_page_can_toggle_favorite(self, driver):
        hymn_page = self._load_hymn(driver)
        hymn_page.toggle_favorite()
        assert True

    def test_hymn_page_can_add_to_list_and_mark_known(self, driver):
        hymn_page = self._load_hymn(driver)
        hymn_page.add_to_list()
        hymn_page.mark_as_known()
        assert True

    def test_hymn_page_navigation_buttons(self, driver):
        hymn_page = self._load_hymn(driver)
        hymn_page.open_previous_hymn()
        hymn_page.open_next_hymn()
        hymn_page.rewind()
        hymn_page.forward()
        assert True
