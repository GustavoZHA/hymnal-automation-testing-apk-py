---
name: implementar-page-object
description: Implementación de Page Objects en pages/ heredando de BasePage o MenuComponent con esperas explícitas y sin aserciones.
---

# Skill: Implementar Page Objects

Este skill define las directrices para codificar y extender las clases de página (**Page Object Model**) en el directorio `pages/`.

---

## 🎯 Reglas de Oro de los Page Objects

1. **Responsabilidad Única**: El Page Object encapsula la **estructura y las acciones** de una pantalla. Nunca debe contener lógica de negocio de la prueba ni aserciones (`assert`).
2. **Herencia**:
   - Heredar de `BasePage` para pantallas aisladas.
   - Heredar de `MenuComponent` si la pantalla comparte la barra de navegación superior (botón Home y Navigation Drawer).
3. **Cero `time.sleep()`**: Toda interacción debe valerse de los métodos base (`self.click()`, `self.get_text()`, `self.wait_for_element()`) que emplean `WebDriverWait` explícito.
4. **Retornos Fluidos (Page Chaining)**:
   - Si una acción navega a otra pantalla, el método debe retornar la instancia de la nueva página:
     ```python
     def open_hymnal(self) -> HymnListPage:
         self.click(HomeLocators.HYMNAL_BUTTON)
         return HymnListPage(self.driver)
     ```
   - Si la acción mantiene al usuario en la misma pantalla o en un popup, retornar `self`:
     ```python
     def add_to_list(self):
         self.click(HymnPageLocators.ADD_TO_LIST_BUTTON)
         return self
     ```
5. **Limpieza de Inputs**: Antes de escribir en un `EditText`, siempre limpiar el campo (`self.clear_text()` o `element.clear()`).

---

## 🏗️ Plantilla de un Page Object

```python
from pages.base_page import BasePage
from pages.components.menu_component import MenuComponent
from locators.mi_modulo_locators import MiModuloLocators
from pages.otra_pantalla_page import OtraPantallaPage

class MiModuloPage(MenuComponent):
    """Representa la pantalla del módulo X en Hymnal App."""

    def enter_query(self, query: str) -> "MiModuloPage":
        self.type_text(MiModuloLocators.QUERY_INPUT, query)
        return self

    def click_submit(self) -> OtraPantallaPage:
        self.click(MiModuloLocators.SUBMIT_BUTTON)
        return OtraPantallaPage(self.driver)

    def get_title_text(self) -> str:
        return self.get_text(MiModuloLocators.TITLE)

    def is_element_visible(self) -> bool:
        return self.is_displayed(MiModuloLocators.ELEMENT)

    def get_toast_message(self) -> str:
        return self.get_text(MiModuloLocators.TOAST_MESSAGE)
```

---

## 📋 Checklist de Validación

- [ ] ¿La clase hereda adecuadamente de `BasePage` o `MenuComponent`?
- [ ] ¿No contiene ninguna sentencia `assert`?
- [ ] ¿Usa esperas explícitas y no pausas estáticas (`time.sleep`)?
- [ ] ¿Los métodos devuelven objetos de página o valores de inspección claros (`str`, `bool`, `list`)?
- [ ] ¿Los nombres de los métodos describen intenciones del usuario (`open_...`, `select_...`, `get_...`)?
