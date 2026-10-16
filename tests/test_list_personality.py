from datetime import datetime

import allure
import pytest

from pages.home_page import HomePage
from pages.hymn_list_page import HymnListPage
from pages.list_personality_page import ListPersonalityPage
from locators.list_personality_locators import ListPersonalityLocators


@allure.epic("Himnario Móvil")
@allure.feature("Listas Personalizadas")
class TestListPersonality:

    @allure.title("SCN-LST-001: Abrir pantalla de Listas Personalizadas y verificar título")
    def test_open_list_personality_page_and_verify_title(self, driver):
        with allure.step("Dado que el usuario está en el Home"):
            home = HomePage(driver)

        with allure.step("Cuando abre la sección de Listas Personalizadas"):
            list_personality = home.open_list_personality()

        with allure.step("Entonces la pantalla está visible y el título es 'Listas Personalizadas'"):
            assert list_personality.is_page_displayed()
            assert list_personality.get_page_title() == "Listas Personalizadas"

    @allure.title("SCN-LST-002: Verificar componentes principales de la pantalla")
    def test_verify_list_personality_page_elements(self, driver):
        with allure.step("Dado que el usuario accede a Listas Personalizadas"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()

        with allure.step("Entonces el campo de entrada de texto y el botón de crear están visibles"):
            assert list_personality.is_displayed(ListPersonalityLocators.NAME_INPUT)
            assert list_personality.is_displayed(ListPersonalityLocators.CREATE_BUTTON)

    @allure.title("SCN-LST-003: Verificar el texto de sugerencia (hint) del campo de nombre")
    def test_verify_name_input_hint_text(self, driver):
        with allure.step("Dado que el usuario accede a Listas Personalizadas"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()

        with allure.step("Cuando consulta el texto de sugerencia (hint) del input"):
            hint_text = list_personality.get_name_input_hint()

        with allure.step("Entonces el hint debe ser 'Escriba el nombre de Lista a Crear'"):
            assert hint_text == "Escriba el nombre de Lista a Crear"

    @allure.title("SCN-LST-004: Limpiar el campo de texto de nombre de lista")
    def test_clear_name_input_field(self, driver):
        with allure.step("Dado que el usuario ingresa un texto en el campo de nombre de lista"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()
            list_personality.enter_list_name("Test Text")

        with allure.step("Cuando limpia el campo de texto"):
            list_personality.clear_name_input()

        with allure.step("Entonces el campo muestra el texto por defecto o queda vacío"):
            field_text = list_personality.driver.find_element(*ListPersonalityLocators.NAME_INPUT).text
            assert field_text in "Escriba el nombre de Lista a Crear"

    @allure.title("SCN-LST-005: Crear una nueva lista personalizada exitosamente")
    def test_create_new_personalized_list(self, driver):
        list_name = "CNL" + datetime.now().strftime("%H:%M:%S.%f")[:-3]

        with allure.step("Dado que el usuario accede a Listas Personalizadas"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()

        with allure.step(f"Cuando ingresa el nombre '{list_name}' y pulsa el botón crear"):
            list_personality.create_new_list(list_name)

        with allure.step("Entonces se muestra un mensaje Toast confirmando la creación exitosa"):
            toast_text = list_personality.get_toast_message()
            assert "creada exitosamente" in toast_text

    @allure.title("SCN-LST-006: Eliminar una lista personalizada existente")
    def test_delete_personalized_list(self, driver):
        list_name = "CNL" + datetime.now().strftime("%H:%M:%S.%f")[:-3]

        with allure.step(f"Dado que se crea una lista previa con nombre '{list_name}'"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()
            list_personality.create_new_list(list_name)
            toast = list_personality.get_toast_message()
            assert "creada exitosamente" in toast

        with allure.step("Y el usuario regresa a Home y vuelve a abrir Listas Personalizadas"):
            home.click_home_button()
            list_personality = home.open_list_personality()

        with allure.step(f"Cuando el usuario elimina la lista recién creada '{list_name}'"):
            list_personality.delete_list_by_name(list_name)

        with allure.step(f"Entonces la lista '{list_name}' ya no debe estar visible"):
            assert not list_personality.is_list_name_visible(list_name)

    @allure.title("SCN-LST-007: Agregar un himno a una lista personalizada y verificar su presencia")
    def test_add_hymn_to_personalized_list(self, driver):
        list_name = "TAL" + datetime.now().strftime("%H:%M:%S.%f")[:-3]
        hymn_title = "Cantemos aqui"

        with allure.step(f"Dado que se crea una nueva lista personalizada '{list_name}'"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()
            list_personality.create_new_list(list_name)
            toast_text = list_personality.get_toast_message()
            assert "creada exitosamente" in toast_text

        with allure.step(f"Cuando se navega al himnario, se abre el himno '{hymn_title}' y se agrega a la lista '{list_name}'"):
            list_personality.click_home_button()
            home = HomePage(driver)
            hymn_list_page = home.open_hymnal()
            hymn = hymn_list_page.open_hymn_by_title(hymn_title)
            hymn.add_to_list()
            hymn.select_list_from_popup(list_name)
            hymn.click_home_button()

        with allure.step(f"Y se abre la lista personalizada '{list_name}'"):
            home = HomePage(driver)
            list_personality = home.open_list_personality()
            list_personality.click_list_by_name(list_name)

        with allure.step(f"Entonces el himno '{hymn_title}' está presente en el listado"):
            hymn_list_page = HymnListPage(driver)
            hymn_names = hymn_list_page.get_all_hymn_names()
            assert hymn_title in hymn_names, f"El himno '{hymn_title}' no se encontró en la lista"
