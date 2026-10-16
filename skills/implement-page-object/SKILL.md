---
name: implement-page-object
description: Page Object implementation in pages/ inheriting from BasePage or MenuComponent with explicit waits and no assertions.
---

# Skill: Implement Page Objects (POM)

This skill defines the architectural guidelines and design patterns for creating and extending Page Objects in the `pages/` directory.

---

## 🎯 Core Rules of Page Objects

1. **Single Responsibility**: A Page Object represents the **structure and interactions** of a screen or component. It must never contain test assertions (`assert`) or business validation logic.
2. **Inheritance**:
   - Inherit from `BasePage` for standalone screens.
   - Inherit from `MenuComponent` if the screen shares the top navigation bar (Home button and Navigation Drawer).
3. **Zero `time.sleep()`**: All element interactions must leverage BasePage methods (`self.click()`, `self.get_text()`, `self.wait_for_element()`), which use explicit `WebDriverWait`.
4. **Fluent Page Chaining**:
   - If an action transitions to a new screen, return the new Page Object instance:
     ```python
     def open_hymnal(self) -> HymnListPage:
         self.click(HomeLocators.HYMNAL_BUTTON)
         return HymnListPage(self.driver)
     ```
   - If the action stays on the same page or interacts with an inline popup/element, return `self`:
     ```python
     def add_to_list(self):
         self.click(HymnPageLocators.ADD_TO_LIST_BUTTON)
         return self
     ```
5. **Input Sanitation**: Always clear input fields before typing (`self.clear_text()` or `element.clear()`).

---

## 🏗️ Page Object Template

```python
from pages.base_page import BasePage
from pages.components.menu_component import MenuComponent
from locators.search_locators import SearchLocators
from pages.hymn_page import HymnPage

class SearchPage(MenuComponent):
    """Page Object representing the Hymn Search screen."""

    def enter_search_query(self, query: str) -> "SearchPage":
        self.type_text(SearchLocators.SEARCH_INPUT, query)
        return self

    def click_search(self) -> "SearchPage":
        self.click(SearchLocators.SEARCH_BUTTON)
        return self

    def open_hymn_result(self, hymn_number: int) -> HymnPage:
        self.click(SearchLocators.result_item_by_number(hymn_number))
        return HymnPage(self.driver)

    def get_toast_message(self) -> str:
        return self.get_text(SearchLocators.TOAST_MESSAGE)

    def is_search_input_displayed(self) -> bool:
        return self.is_displayed(SearchLocators.SEARCH_INPUT)
```

---

## 📋 Validation Checklist

- [ ] Does the class properly inherit from `BasePage` or `MenuComponent`?
- [ ] Is the Page Object completely free of `assert` statements?
- [ ] Are explicit waits used rather than static sleeps?
- [ ] Do methods return Page Object instances or clean primitives (`str`, `bool`, `list`)?
- [ ] Are method names descriptive and written in English (`open_...`, `get_...`, `is_..._displayed`)?
