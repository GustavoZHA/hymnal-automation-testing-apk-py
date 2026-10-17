import json
from pathlib import Path

import allure
import pytest

from pages.home_page import HomePage


DATA_DIR = Path(__file__).resolve().parents[1] / "resources" / "test_data"
EXPECTED_FILE = DATA_DIR / "classification_expected.json"


def load_expected_classification():
    with open(EXPECTED_FILE, encoding="utf-8") as file:
        return json.load(file)


@allure.epic("Hymnal Mobile App")
@allure.feature("Clasificación")
class TestClassification:

    @allure.title("SCN-CLA-001: Open Thematic Classification screen and verify title")
    def test_open_classification_screen(self, driver):
        with allure.step("Given the expected classification data is loaded from test resources"):
            expected = load_expected_classification()

        with allure.step("When the user opens the Thematic Classification screen from Home"):
            home = HomePage(driver)
            classification = home.open_classification()

        with allure.step("Then the screen title must match the expected title"):
            actual_title = classification.get_title()
            assert actual_title == expected["title"], (
                f"Expected title '{expected['title']}', but got '{actual_title}'"
            )

    @allure.title("SCN-CLA-002: Open and verify display of a specific thematic category")
    def test_open_classification_category(self, driver):
        with allure.step("Given a thematic category is retrieved from the dataset"):
            expected = load_expected_classification()
            category = expected["categories"][5]

        with allure.step(f"When the user opens Classification and selects category '{category}'"):
            home = HomePage(driver)
            classification = home.open_classification()
            classification.open_category(category)

        with allure.step(f"Then category '{category}' is displayed properly"):
            assert classification.is_category_displayed(category), (
                f"Category '{category}' was not displayed on the screen"
            )

    @allure.title("SCN-CLA-003: Verify total number of thematic categories matches expected catalog")
    def test_classification_categories_count(self, driver):
        with allure.step("Given the expected classification data is loaded"):
            expected = load_expected_classification()
            expected_count = len(expected["categories"])

        with allure.step("When the user opens the Thematic Classification screen"):
            home = HomePage(driver)
            classification = home.open_classification()

        with allure.step(f"Then the expected category catalog contains {expected_count} categories"):
            assert expected_count == 11, f"Expected 11 thematic categories, but found {expected_count}"
            assert classification.get_title() == expected["title"], (
                f"Expected title '{expected['title']}', but got '{classification.get_title()}'"
            )
