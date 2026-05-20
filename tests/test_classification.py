import json
from pathlib import Path

from pages.home_page import HomePage


DATA_DIR = Path(__file__).resolve().parents[1] / "resources" / "test_data"
EXPECTED_FILE = DATA_DIR / "classification_expected.json"


def load_expected_classification():
    with open(EXPECTED_FILE, encoding="utf-8") as file:
        return json.load(file)


class TestClassification:

    def test_open_classification_screen(self, driver):
        expected = load_expected_classification()

        home = HomePage(driver)
        classification = home.open_classification()

        assert classification.get_title() == expected["title"]

    def test_open_classification_category(self, driver):
        expected = load_expected_classification()
        category = expected["categories"][5]

        home = HomePage(driver)
        classification = home.open_classification()
        classification.open_category(category)

        assert classification.is_category_displayed(category)
