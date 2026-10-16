---
name: escribir-test-allure
description: Redacción de casos de prueba en tests/ con Pytest y Allure BDD, integrando el código del escenario (SCN-xxx) en el título y los pasos definidos.
---

# Skill: Escribir Tests con Allure BDD

Este skill define la estructura, reglas y buenas prácticas para la codificación de casos de prueba en el directorio `tests/` utilizando **Pytest** y **Allure BDD**, vinculando directamente la definición previa del escenario con la ejecución.

---

## 🎯 Regla Fundamental: Código BDD en el Título

El identificador único normalizado (`SCN-<MODULO>-<NUM>`) establecido en el skill `definir-escenario-bdd` **debe colocarse obligatoriamente al inicio del título de Allure**:

```python
@allure.title("<CODIGO_SCN>: <Título autoexplicativo>")
```

### Ejemplos de Nomenclatura del Título:
- `@allure.title("SCN-HOM-001: Abrir lista de himnos desde el botón principal del Home")`
- `@allure.title("SCN-BUS-002: Validar mensaje al ingresar texto menor a 5 caracteres")`
- `@allure.title("SCN-FAV-002: Agregar himno a favoritos y verificar su apertura desde la lista de Favoritos")`

> **Beneficio**: En el reporte interactivo de Allure, el árbol de ejecución muestra directamente el ID normalizado, permitiendo una trazabilidad 1:1 inmediata con la matriz de [**`docs/test_scenarios.md`**](file:///f:/Programming/GitHubCode-GutavoZHA/hymnal-automation-testing-apk-py/docs/test_scenarios.md) sin ambigüedades.

---

## 🧩 Implementación de los Pasos BDD (`allure.step`)

El cuerpo de la función de prueba debe materializar los pasos definidos en `definir-escenario-bdd` utilizando bloques `with allure.step(...)`:

1. **Dado (Given)**: Configuración inicial, instanciación de páginas o estado inicial de la pantalla.
2. **Cuando (When)**: Interacción del usuario que desencadena el comportamiento (clic, escritura, scroll).
3. **Y (And)**: Pasos de acción intermedios o complementarios (opcional).
4. **Entonces (Then)**: Verificación o aserción final determinista sobre la interfaz.

---

## 🏗️ Estructura Completa de un Caso de Prueba

```python
import allure
import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage

@allure.epic("Himnario Móvil")
@allure.feature("Búsqueda de Himnos")
class TestSearchPage:

    @allure.title("SCN-BUS-002: Validar mensaje al ingresar texto menor a 5 caracteres")
    def test_search_hymn_by_short_text_shows_validation_toast(self, driver):
        search_query = "des"

        with allure.step("Dado que el usuario está en la pantalla de búsqueda"):
            home = HomePage(driver)
            search_page = home.open_search()

        with allure.step(f"Cuando busca con un texto corto '{search_query}'"):
            search_page.search_hymn(search_query)

        with allure.step("Entonces se muestra el mensaje Toast de validación de longitud mínima"):
            toast_text = search_page.get_toast_message()
            assert toast_text == "El texto debe tener más de 5 caracteres", f"Mensaje Toast incorrecto: '{toast_text}'"
```

---

## ⚠️ Reglas de Aserción y Limpieza

1. **Aserciones Deterministas con Mensaje**:
   - **Prohibido**: `assert True`.
   - **Requerido**: Comparaciones concretas con mensaje de fallo informativo:
     ```python
     assert actual_title == expected_title, f"Se esperaba '{expected_title}' pero se obtuvo '{actual_title}'"
     ```
2. **Validación de Toasts y Mensajes del Sistema**:
   - Usar `.startswith()` o `in` cuando el Toast contenga partes dinámicas (ej. rangos numéricos o timestamps).
3. **Cero Importaciones Huérfanas**:
   - Mantener imports limpios exclusivamente de `pages/`, `locators/`, `utils/`, `allure` y `pytest`.
4. **Sin `@allure.description` Redundante**:
   - Como el título ya contiene el ID y la descripción precisa, no se agrega descripción redundante.

---

## 📋 Checklist de Validación

- [ ] ¿El decorador `@allure.title(...)` incluye el código normalizado al inicio (`SCN-MOD-xxx: Título`)?
- [ ] ¿El código coincide exactamente con el registrado en `docs/test_scenarios.md`?
- [ ] ¿Los bloques `with allure.step(...)` reflejan los pasos Dado / Cuando / Y / Entonces acordados?
- [ ] ¿El test recibe la fixture `driver`?
- [ ] ¿Todas las aserciones son deterministas y tienen mensajes explicativos de error?
