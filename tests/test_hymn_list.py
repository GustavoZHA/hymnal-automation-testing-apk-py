from pages.home_page import HomePage


class TestHymnList:

    def test_open_hymn_list_and_open_by_title(self, driver):
        home = HomePage(driver)
        hymn_list = home.open_hymnal()
        hymn_page = hymn_list.open_hymn_by_title("Ven , ¡oh Todopoderoso!")

        assert hymn_page.get_title() != ""

    def test_open_hymn_list_and_open_by_number(self, driver):
        home = HomePage(driver)
        hymn_list = home.open_hymnal()
        hymn_page = hymn_list.open_hymn_by_number(1)

        assert hymn_page.get_title() == "1. Ven , ¡oh Todopoderoso!"
