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


@allure.epic("Himnario Móvil")
@allure.feature("Clasificación")
class TestClassification:

    @allure.title("SCN-CLA-001: Verificar apertura de la pantalla de Clasificación y su título")
    def test_open_classification_screen(self, driver):
        with allure.step("Dado que se cargan los datos esperados de clasificación"):
            expected = load_expected_classification()

        with allure.step("Cuando el usuario ingresa a la sección de Clasificación desde el Home"):
            home = HomePage(driver)
            classification = home.open_classification()

        with allure.step("Entonces el título de la pantalla debe coincidir con el esperado"):
            actual_title = classification.get_title()
            assert actual_title == expected["title"], f"Se esperaba '{expected['title']}' pero se obtuvo '{actual_title}'"

    @allure.title("SCN-CLA-002: Abrir y verificar la visualización de una categoría específica")
    def test_open_classification_category(self, driver):
        with allure.step("Dado que se obtiene una categoría de prueba desde el archivo de datos"):
            expected = load_expected_classification()
            category = expected["categories"][5]

        with allure.step(f"Cuando el usuario abre Clasificación y selecciona la categoría '{category}'"):
            home = HomePage(driver)
            classification = home.open_classification()
            classification.open_category(category)

        with allure.step(f"Entonces la categoría '{category}' debe estar desplegada correctamente"):
            assert classification.is_category_displayed(category), f"La categoría '{category}' no se mostró en pantalla"
