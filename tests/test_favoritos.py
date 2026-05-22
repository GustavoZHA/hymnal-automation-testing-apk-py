from turtle import home

from pages.home_page import HomePage
from pages.favoritos_page import FavoritosPage
from pages.hymn_page import HymnPage


class TestFavoritos:

    def test_open_favoritos(self, driver):
        """Test opening the Favoritos page from home"""
        home = HomePage(driver)
        home.open_favorites()
        favoritos = FavoritosPage(driver)
        assert favoritos.get_title() == "Favoritos"

    def test_open_hymn_by_title_from_favoritos(self, driver):
        """Test opening a hymn from Favoritos by title"""
        hymn_title = "Alma mía no delires"

        home = HomePage(driver)
        hymnListPage = home.open_hymnal()
        hymnListPage.open_hymn_by_title(hymn_title).toggle_favorite()
        hymnListPage.click_home_button()
        home.open_favorites()
        favoritos = FavoritosPage(driver)
        hymn_page = favoritos.open_hymn_by_title(hymn_title)
        assert hymn_title in hymn_page.get_title()
        assert isinstance(hymn_page, HymnPage)

    def test_navigate_from_favoritos_to_home(self, driver):
        """Test navigating from Favoritos back to home page"""
        home = HomePage(driver)
        home.open_favorites()
        favoritos = FavoritosPage(driver)
        home_page = favoritos.go_to_home()
        assert isinstance(home_page, HomePage)
