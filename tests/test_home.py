from pages.home_page import HomePage


class TestHome:

    def test_open_hymnal(self, driver):
        home = HomePage(driver)
        home.open_hymnal()
        assert True
