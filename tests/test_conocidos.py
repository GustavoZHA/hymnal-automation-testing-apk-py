from pages.home_page import HomePage
from pages.conocidos_page import ConocidosPage
from pages.hymn_page import HymnPage


class TestConocidos:

    def test_open_conocidos(self, driver):
        """Test opening the Conocidos page from home"""
        home = HomePage(driver)
        home.open_known()
        conocidos = ConocidosPage(driver)
        assert conocidos.get_title() == "Conocidos"

    def test_open_and_add_hymn_in_conocidos(self, driver):
        """Test opening a hymn from Conocidos by number"""
        hymn_number = 12
        hymn_title = "Cúan firme cimiento"

        home = HomePage(driver)
        hymnListPage = home.open_hymnal()
        hymnListPage.open_hymn_by_number(hymn_number).mark_as_known()
        hymnListPage.click_home_button()
        home.open_known()
        conocidos = ConocidosPage(driver)
        hymn_page = conocidos.open_hymn_by_number(hymn_number)
        assert f"{hymn_number}" in hymn_page.get_title()
        assert hymn_title in hymn_page.get_title()
        assert isinstance(hymn_page, HymnPage)

    def test_navigate_from_conocidos_to_home(self, driver):
        """Test navigating from Conocidos back to home page"""
        home = HomePage(driver)
        home.open_known()
        conocidos = ConocidosPage(driver)
        home_page = conocidos.go_to_home()
        assert isinstance(home_page, HomePage)
