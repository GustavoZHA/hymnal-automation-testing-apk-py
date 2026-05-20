from pages.home_page import HomePage
from pages.hymn_list_page import HymnListPage


class TestHome:

    def test_open_hymnal(self, driver):
        home = HomePage(driver)
        home.open_hymnal()
        assert True

    def test_open_hymn_by_title(self, driver):
        home = HomePage(driver)
        home.open_hymnal()

        hymn_list = HymnListPage(driver)
        hymn_list.open_hymn_by_title("Ven , ¡oh Todopoderoso!")
        assert True
