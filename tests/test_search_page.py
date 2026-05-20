from pages.home_page import HomePage
from locators.search_locators import SearchLocators


class TestSearchPage:

    def test_open_search_page_and_verify_elements(self, driver):
        home = HomePage(driver)
        search_page = home.open_search()

        assert search_page.is_displayed(SearchLocators.SEARCH_INPUT)
        assert search_page.is_displayed(SearchLocators.SEARCH_BUTTON)

    def test_search_hymn_by_short_text_shows_validation_toast(self, driver):
        home = HomePage(driver)
        search_page = home.open_search()
        search_page.search_hymn("des")

        toast_text = search_page.get_toast_message()
        assert toast_text == "El texto debe tener más de 5 caracteres"

    def test_search_hymn_by_number_out_of_range_shows_validation_toast(self, driver):
        home = HomePage(driver)
        search_page = home.open_search()
        search_page.search_hymn("9999")

        toast_text = search_page.get_toast_message()
        assert toast_text.startswith("El número debe estar entre 1 al ")

    def test_search_hymn_by_mixed_input_shows_validation_toast(self, driver):
        home = HomePage(driver)
        search_page = home.open_search()
        search_page.search_hymn("12abc")

        toast_text = search_page.get_toast_message()
        assert toast_text == "No se permite mezclar texto y números"

    def test_search_hymn_by_invalid_characters_shows_general_validation_toast(self, driver):
        home = HomePage(driver)
        search_page = home.open_search()
        search_page.search_hymn("@@@")

        toast_text = search_page.get_toast_message()
        assert toast_text.startswith("Solo se permite texto o números entre 1 al ")

    def test_search_hymn_by_number_and_open_result(self, driver):
        home = HomePage(driver)
        search_page = home.open_search()
        search_page.search_hymn("1")

        assert search_page.get_results_count() > 0

        hymn_page = search_page.open_hymn_by_number(1)
        assert hymn_page.get_title() != ""
