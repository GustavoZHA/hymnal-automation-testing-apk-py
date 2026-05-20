from pages.home_page import HomePage
from pages.components.menu_component import MenuComponent


class TestHomeActions:

    def test_open_search(self, driver):
        home = HomePage(driver)
        home.open_search()
        assert True

    def test_open_favorites(self, driver):
        home = HomePage(driver)
        home.open_favorites()
        assert True

    def test_open_known(self, driver):
        home = HomePage(driver)
        home.open_known()
        assert True

    def test_open_personalized_lists(self, driver):
        home = HomePage(driver)
        home.open_personalized_lists()
        assert True

    def test_open_menu_and_home(self, driver):
        menu = MenuComponent(driver)
        menu.open_drawer()
        menu.click_home_button()
        assert True
